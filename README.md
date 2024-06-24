### Problem: I don't know when I can buy rösti
# I'm a fan of rösti but it's only sold during alpine-themed weeks at my local supermarket. I don't go to that supermarket every week and I don't want to sign up for marketing emails so I don't know when it's available.

### Solution: Check a webpage to tell me what this week's theme is and send an email
# A simply web scraper script that uses BeautifulSoul checks the supermarket's offers website and sends an email if it seems that alpine week is listed as the flavour of the week. 
# The script is hosted on AWS Lambda. It is triggered every Monday with AWS Eventbridge and uses AWS Simple Email Service to send me an alert.