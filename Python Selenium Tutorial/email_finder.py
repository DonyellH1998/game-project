from selenium import webdriver
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH) 

driver.get("https://mikurestaurant.com/contactus/")

page = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', page)

for email in emails:
    print(email)