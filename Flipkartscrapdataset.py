#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[2]:


# Connect to Website and pull in data

URL = 'https://www.flipkart.com/vebnor-printed-men-polo-neck-light-blue-t-shirt/p/itm5a92ca3566ecc?pid=TSHGR4RYGPHDUYRG&lid=LSTTSHGR4RYGPHDUYRGSUWAMI&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_1&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion~Men%27s%2BTop%2BWear~Men%27s%2BT-Shirts_IF56C41VGEYS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=en_AR4T75fPYAKJ0_eYTVoRd_YtCcgKqidrELTlcDYr6RJJbjs3ikqDavSVMEje90xEmvCkJcF-42i8dxnOBDBsNA%3D%3D&ppt=None&ppn=None&ssid=44mhyg4lf40000001731089304184'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(class_="VU-ZEz").get_text()

price = soup2.find(class_="Nx9bqj CxhGGd").get_text()


print(title)
print(price)


# In[3]:


# Clean up the data a little bit

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[4]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[6]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('FlipkartWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
    print("data writing succesfull")
    


# In[8]:


import pandas as pd

df = pd.read_csv(r'C:\Users\zamee\FlipkartWebScraperDataset.csv')

print(df)


# In[9]:


#Now we are appending data to the csv

with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[10]:


def check_price():
    URL = 'https://www.flipkart.com/vebnor-printed-men-polo-neck-light-blue-t-shirt/p/itm5a92ca3566ecc?pid=TSHGR4RYGPHDUYRG&lid=LSTTSHGR4RYGPHDUYRGSUWAMI&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_1&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion~Men%27s%2BTop%2BWear~Men%27s%2BT-Shirts_IF56C41VGEYS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=en_AR4T75fPYAKJ0_eYTVoRd_YtCcgKqidrELTlcDYr6RJJbjs3ikqDavSVMEje90xEmvCkJcF-42i8dxnOBDBsNA%3D%3D&ppt=None&ppn=None&ssid=44mhyg4lf40000001731089304184'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(class_="VU-ZEz").get_text()

    price = soup2.find(class_="Nx9bqj CxhGGd").get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
#         if(price < 300):
#             send_mail()
        
 


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(rr'C:\Users\zamee\FlipkartWebScraperDataset.csv')

print(df)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script
if (price < 300):
    send_mail()
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('sa3551834@gmail.com','Sayyedalam@&6386')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sa3551834@gmail.com',
        msg
     
    )


# In[ ]:




