import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

# strftime changes day time object to string type
from_datetime = datetime.strptime(from_date, '%Y/%m/%d') # strptime changes string object time to day Time type
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple())) # time.mktime changes time format to epoch time format
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
# header is used to Impersonate in the web otherwise permission will be denied

content_binary = requests.get(url, headers=headers).content # get the content from the url of given datta table
print(content_binary)

with open("data_binary.csv", "wb") as file:  # "wb" stands for write binary file, it can be a file with binary data
    file.write(content_binary)

content_text = requests.get(url, headers=headers).text
print(content_text)

with open("data_text.csv", "w")as file: # w stands for only write text, it could be mainly text file
    file.write(content_text)
