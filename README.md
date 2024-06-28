~~# Problem: I don't know when I can buy rösti
I'm a fan of rösti but it's only sold during alpine-themed weeks at my local supermarket. I don't go to that supermarket every week and I don't want to sign up for marketing emails so I don't know when it's available.~~

~~# Solution: Check a webpage to tell me what this week's theme is and send an email
A simple web scraper script that uses the BeautifulSoup library checks the supermarket's offers website and sends an email if it seems that alpine week is listed as the flavour of the week. 
The script is hosted on AWS Lambda. It is triggered every Monday with AWS Eventbridge and uses AWS Simple Email Service to send me an alert.~~

*"If at first you don't succeed, start the project again with **new_** in front of it"* --> [new_rosti_scraper](https://github.com/fantastito/new_rosti_scraper)

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![AWS Lambda Badge](https://img.shields.io/badge/AWS%20Lambda-F90?logo=awslambda&logoColor=fff&style=flat) ![Amazon Simple Email Service Badge](https://img.shields.io/badge/Amazon%20Simple%20Email%20Service-DD344C?logo=amazonsimpleemailservice&logoColor=fff&style=flat)
