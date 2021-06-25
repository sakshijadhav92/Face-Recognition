#we need pywhatkit module for this 
#pip install pywhatkit


# importing the module
from datetime import datetime
import pywhatkit
# using Exception Handling to avoid 
# unprecedented errors
try:
    now = datetime.now()
    hours = int(now.strftime("%H"))
    type_hour = type(hours)
    print(type_hour)
    print("Current Time =", hours)
    minutes = int(now.strftime("%M")) + 2
    type_minutes = type(minutes)
    print(type_minutes)
    print("Current Time =", minutes)
    # sending message to receiver 
    pywhatkit.sendwhatmsg("+91XXXXXXXXXX" , "Hey , We have Sent the whatsapp Message. ",hours,minutes)
except:
    # printing error message
    print("An Unexpected Error!")
    

'''
pywhatkit.sendmsg(“receiver mobile number”,”message”,hours,minutes)
Parameters:
Receiver mobile number: The Receiver’s mobile number must be in string format and the country code must be mentioned before the mobile number.
Message: Message to be sent(Must be in string format).
Hours: This module follows the 24 hrs time format.
Minutes: Mention minutes of the scheduled time for the message(00-59).
'''
