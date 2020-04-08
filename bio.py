'''Twitter bioBot developed by Jordan Cannon'''
from keys import getApi
import os
from datetime import date, datetime
import time
# Create API object
api = getApi()
# Get number of days since I was born
def numOfDays(dt1, dt2):
    return (dt2-dt1).days
while True:
# Establish some variables
#Todays date
    today = date.fromtimestamp(time.time())
#Birth month and todays date into an object
    dt1 = date(0, 0, 0) '''Set this as your birthday'''
    dt2 = date(today.year, today.month, today.day)
# Some more variables for hour, minute, and second. As well as casting some integers
    hr = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    rn = ((int(hr) * 3600) + (int(min) * 60) + int(sec))
# Convert the time into seconds and sets bio variable
    secsConversion = ((numOfDays(dt1, dt2)) * 86400) + rn
    bio = "I've been alive for : " + str(secsConversion) + " seconds.")
    api.update_profile(description=bio)
    print(secsConversion),
    time.sleep(20.1) '''Do not change this time, used for bypassing rate limiting'''
