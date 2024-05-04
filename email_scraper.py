from selenium import webdriver
import json
from webdriver_manager.firefox import GeckoDriverManager
import os
import sys
from selenium.webdriver.firefox.options import Options
import re 
import time
from selenium.webdriver.common.by import By
import form_iden
import json_converter
import json_save
import pandas as pd
folder_path=r"D:\email_extraction project"
excel_folder = r"D:\email_extraction project"
current_time = time.strftime("%H_%M_%S", time.localtime())
def json_to_excel(folder_path, filename, excel_folder, filenameex):
    try:
        
        # Construct full file paths
        json_filepath = os.path.join(folder_path, filename)
        excel_filepath = os.path.join(excel_folder, filenameex)

        # Check if the JSON file exists
        if not os.path.isfile(json_filepath):
            print(f"Error: '{json_filepath}' does not exist.")
            return

        # Try to open the JSON file
        with open(json_filepath, 'r') as file:
            data_js = json.load(file)             
        # Convert JSON to DataFrame
            df = pd.json_normalize(data_js)
            # Write DataFrame to Excel
            df.to_excel(excel_filepath, index=False)

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist or could not be opened.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}") 
def initialize_driver():
    gecko_driver_path = GeckoDriverManager().install()
    options = Options()
    options.set_preference("browser.privatebrowsing.autostart", True)
    options.add_argument("--headless")
    options.add_argument("-private")  # Open in private browsing mode
    driver = webdriver.Firefox(options=options)
    os.environ["webdriver.gecko.driver"] = gecko_driver_path
    return driver   
driver=initialize_driver()
form=[]
email_address=""
folder_path = r"D:\email_extraction project"
def final(websites,url,list_of_printed_cars):
    filenameex=f"{current_time}email_list.xlsx"
    filenameex = re.sub(r'[^\w\.-]', '_', filenameex)
    filename = f"email_list.json"
    list_of_emails=[]
    def anik():
        try:
            for mail in websites:
                time.sleep(0.2) 
                print(mail)      
                if len(list_of_emails)==1:
                    break
                driver.get(mail)   
                #EMAIL_REGEX=r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
                EMAIL_REGEX=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
                #EMAIL_REGEX=r'[a-zA-Z0-9._%+-]+\s+at\s+[a-zA-Z0-9.-]+\s+dot\s+[a-zA-Z]{2,}'#this one for at dot
                #EMAIL_REGEX=r'[A-Za-z0-9.#_%+-]+@[-]+'
                page_source=driver.page_source
                for re_match in re.finditer (EMAIL_REGEX, page_source): 
                    anik=re_match.group()
                    if len(list_of_emails)==1:
                        break              
                    elif anik not in list_of_emails and all(substring not in str(anik) for substring in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg" ,"someone","domain","email","example","sentry"]):
                        list_of_emails.append(anik)          
                        print(list_of_emails)
                        return{
                            "domain":url,
                            "email_address":anik
                        }             
        except:
            return{
                    "domain":url,
                    "email_address":"no _email_found"
                }  
        return {
        "domain": url,
        "email_address": "no_email_found"
    }                      
    anik=anik()
    json_save.save(anik,filename,folder_path,json,os,list_of_printed_cars)
    json_to_excel(folder_path, filename, excel_folder, filenameex)

