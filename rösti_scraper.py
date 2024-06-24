from bs4 import BeautifulSoup
import requests
import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv
import os

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
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")

        #Find this week's offers section
        this_week = soup.find(title="This Week's Offers")

        target_text = "Flavour of the Week"

        #Find the 'Flavour of the Week' card by searching h3 tags for target with string, checking string not empty
        flavour_of_the_week = this_week.find('h3', string=lambda t:t and target_text in t)
        for child in flavour_of_the_week.children:
            print(child)
            if 'Alpen Fest' in child:
                send_email("Get ready for rösti", "It looks like it is Alpen Fest week at Lidl. Go grab some rösti")
            else:
                send_email("No rösti this week", "No rösti in Lidl this week, you'll have to cook something else")