from selenium import webdriver
from selenium.webdriver.common.keys import Keys #importing key functions from keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH) #calling specified driver and browser

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_name("s") #searching through html code for element with specific name
search.clear() #clears text from input field
search.send_keys("test")
search.send_keys(Keys.RETURN)

try: #this try statement waits for certain condition to occur before proceeding
    main = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "main")) #waits for the presence of specified element to be located on the page before continuing with the script
    )                                                   

    articles = main.find_elements_by_tag_name("article")

    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()

