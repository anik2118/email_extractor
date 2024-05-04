from selenium import webdriver
import json
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import os
import sys
from selenium.webdriver.firefox.options import Options
import re 
def initialize_driver():
    gecko_driver_path = GeckoDriverManager().install()
    options = Options()
    options.set_preference("browser.privatebrowsing.autostart", True)
    options.add_argument("-private")  # Open in private browsing mode
    driver = webdriver.Firefox(options=options)
    os.environ["webdriver.gecko.driver"] = gecko_driver_path
    return driver   
driver=initialize_driver()
mail="https://gutzy.asia/contact-us/"
driver.get("https://www.malavida.com/es/contact")
list_of_emails=[]
form=[]
# Find all form elements
def form_identifier():
    try:
        if "contact" in mail and len(list_of_emails)==0:
            email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
            print(email_input)
            if (email_input) :
                print(f"Found form(s) on the page.")
                form.append(mail)
            else:
                print(f"No form(s) on the page")  
    except:
        print("No forms found on the page.")
form_identifier()