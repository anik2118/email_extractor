from selenium.webdriver.common.by import By
# Find all form elements
def form_identifier(mail,driver,list_of_emails):
    try:
        if "contact" in mail and len(list_of_emails)==0:
            email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
            if (email_input) :
                print(f"Found form(s) on the page.")
                return True
            else:
                print(f"No form(s) on the page")  
    except:
        print("No forms found on the page.")
