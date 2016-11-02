""" A script that send an SMS alert about a predefined TimeTabel"""

# imports
from twilio.rest import TwilioRestClient
from datetime import datetime
import time

# Day defeniton
# fill your time and class according to the template below
# day = {Time:class}
# Time = float, class = String
mon = {}
tue = {}
wed = {}
thu = {}
fri = {}
sat = {}
# eg: mon = {9.00:'Drink tea',9:10:'Drink some more tea',10:00:"Shit on @itsharrus code even though I've never come close to finishing a project  in time"}

# week, a dictionary holding the values weekDay and day
# weekDay = day number indexed  from Zero, day = dictionary defined above
week = {0:mon,1:tue,2:wed,3:thu,4:fri,5:sat}

# TwilioRestClient defeniton
# Put your Credentials here
# Go to  "https://www.twilio.com/console/" to get your ACCOUNT_SID and AUTH_TOKEN
ACCOUNT_SID = "YOUR ACCOUNT_SID"
AUTH_TOKEN = "YOUR AUTH_TOKEN"
myNumber = 'YOUR PHONE NUMBER'
twNumner = 'TWILIO PHONE NUMBER'

# initialise clinet
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# function to send an sms
# refer "https://www.twilio.com/docs/api?filter-product=sms&filter-platform=mobile" for more details
def sms_twilio(msg='Test sucesses'):
    client.messages.create(
        to=myNumber,
        from_=twNumner,
        body=msg,
        )

# event loop
while True:
# get current current weekDay and Time
    weekDay = int(datetime.now().strftime('%d'))
    Time = float(datetime.now().strftime('%H.%M'))
# try sending a message unless a KeyError occurs
# i.e only send a message if the time a key in the dictionary
    try:
        sendMessage = 'You have (to)'+week[weekDay][Time]
        sms_twilio(sendMessage)
    except KeyError:
        pass
# sleep for a minute , so that when the test case mathches, it sends  only "one" message
    time.sleep(60)

# a delta of about 10 seconds will be present (from actual time) depending on when you run the script,
# so make that your times are a few minutes ahed of schedule.
