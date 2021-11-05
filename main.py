#to download all the bhavzip files form NSE website 
import io
import os
import os.path
import zipfile
import datetime as dt
from urllib import request
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from dateutil import rrule
import requests
import urllib.request
import pandas as pd
from requests.models import Response
from unzipper import unzipper

list_of_files = []
list_of_files_for_unzipper = []
bhavcopy_base_url = "https://www1.nseindia.com/content/historical/EQUITIES/%s/%s/cm%s%s%sbhav.csv.zip"
bhavcopy_base_filename = "cm%s%s%sbhav.zip"
bhavcopy_base_filename_csv = "cm%s%s%sbhav.csv"

def date_range_fnc(frm):
    frm = parse(frm).date()
    to = dt.date.today()
    date_list  = []
    for date in rrule.rrule(rrule.DAILY, dtstart=frm, until=to, byweekday=[0, 1, 2, 3, 4]):
        date_list.append(date.date())
    return date_list


list_sample = date_range_fnc("Jan 1") #here we are downloading only the bhavcopy file from Jan 1, you can change this to any date, remember to to check it is aviable in NSE server as they tend to preriodically remove old files 
limit = len(list_sample)
for num in range (0,limit):
    month_name = list_sample[num].strftime("%b").upper()
    calander_day = list_sample[num].strftime("%d")
    year = list_sample[num].year 
    url = bhavcopy_base_url % (year, month_name, calander_day, month_name, year)
    dwn_file_name = bhavcopy_base_filename % (calander_day, month_name, year)
    csv_names_inside = bhavcopy_base_filename_csv % (calander_day, month_name, year)
    print(url) #just for debugging and to know the script is working
    if os.path.exists(dwn_file_name) is False: #checking if the file exists or not
        response = requests.get(url) 
        if response.ok: #checking if the bhavcopy is alredy uploaded to the server
            list_of_files.append(csv_names_inside)
            list_of_files_for_unzipper.append(dwn_file_name) # this for the next script unzipper to select the file
            with open(dwn_file_name, "wb") as zipfile1:
                zipfile1.write(response.content)
        file_name_list = pd.DataFrame(list_of_files)
        file_name_list_for_unzipper = pd.DataFrame(list_of_files_for_unzipper)
        file_name_list.to_csv("filename.csv") 
        file_name_list_for_unzipper.to_csv("filename_zipper.csv")

unzipper()