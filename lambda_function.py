from bs4 import BeautifulSoup
import requests
import boto3
from botocore.exceptions import ClientError

#Send email

def send_email(subject, body):
    client = boto3.client("ses")
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    try:    
        response = client.send_email(
            Source='simon.budden@gmail.com',
            Destination={
                'ToAddresses': [
                    'simon.budden@gmail.com',
                ],
            },
            Message = message
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    

#Trigger AWS Lambda to find if it's alpine week using BeautifulSoup
def lambda_handler(event, context):
    url = "https://www.lidl.co.uk/c/food-offers/s10023092"
    try:    
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")

            #Find this week's offers section
            this_week = soup.find(title="This Week's Offers")
            if this_week:
                target_text = "Flavour of the Week"

                #Find the 'Flavour of the Week' card by searching h3 tags for target with string, checking string not empty
                flavour_of_the_week = this_week.find('h3', string=lambda t:t and target_text in t)
                if flavour_of_the_week:
                    for child in flavour_of_the_week.children:
                        #Happy path
                        if 'Alpen Fest' in child:
                            send_email("Get ready for rösti", "It looks like it is Alpen Fest week at Lidl. Go grab some rösti")
                            return {"statusCode": 200}
                    #Alpen Fest not found
                    send_email("No rösti this week", "No rösti in Lidl this week, you'll have to cook something else")
                    return {"statusCode": 200}
                else:
                    #Flavour of week not found
                    send_email("No Flavour of the Week", "Unable to find 'Flavour of the Week' in Lidl offers this week")
                    return {"statusCode": 200}
            else:
                #Offers section not found
                send_email("No offers section found", "Can't find 'This Week's Offers' section in Lidl offers page")
                return {"statusCode": 200}
        else:
            #Unexpected status code
            send_email("Error accessing Lidl offers", f"Received status code {response.status_code} from Lidl offers page")
            return {"statusCode": response.status_code}
    except requests.RequestException as e:
        #General request exceptions
        send_email("Error accessing Lidl offers", f"Request to Lidl offers page failed: {str(e)}")
        return {"statusCode": 500}
    except Exception as e:
        #Any unexpected exceptions
        send_email("Lambda handler error", f"An unexpected error occurred: {str(e)}")
        return {"statusCode": 500}

def test_run():
    url = "https://www.lidl.co.uk/c/food-offers/s10023092"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")

        #Find this week's offers section
        this_week = soup.find(title="This Week's Offers")
        print(this_week.prettify())
        target_text = "Flavour of the Week"

        #Find the 'Flavour of the Week' card by searching h3 tags for target with string, checking string not empty
        flavour_of_the_week = this_week.find('h3', string=lambda t:t and target_text in t)
        print(this_week.find('h3', string=lambda t:t and target_text in t).prettify())
        for child in flavour_of_the_week.children:
            print(child)
            if 'Alpen Fest' in child:
                print("Success")
            else:
                print("Fail")

# test_run()