from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from time import sleep
import csv

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from csv import DictReader

driver=webdriver.Chrome()
driver.get('https://www.linkedin.com/')
time.sleep(4)

def get_cookies_values(file):
    with open(file, encoding='utf-8-sig') as f:
        dict_reader = DictReader(f)
        list_of_dicts=list(dict_reader)
    return list_of_dicts

time.sleep(2)

cookies=get_cookies_values("linkedin_cookie.csv")

time.sleep(2)

for i in cookies:
    driver.add_cookie(i)

time.sleep(2)
driver.refresh()
time.sleep(3)

def extract_urls(csv_file):
    urls = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Assuming the CSV file has a column named 'URL'
        for row in csv_reader:
            url = row.get('URL')  # Change 'URL' to the actual column name in your CSV
            if url:
                urls.append(url)

    return urls

# Replace 'output1.csv' with your actual CSV file name
csv_file_name = 'output10.csv'

try:
    urls = extract_urls(csv_file_name)
    if urls:
        print("Extracted URLs:")
        for url in urls:
            driver.get(url)
            time.sleep(3)
            all_buttons=driver.find_elements(by=By.TAG_NAME,value="button")
            connect_buttons=[btn for btn in all_buttons if btn.text== "Connect"]
            for btn in connect_buttons:
                    driver.execute_script("arguments[0].click();",btn)
                    time.sleep(2)
            add_note=driver.find_element(by=By.XPATH,value="//button[@aria-label='Add a note']")
            driver.execute_script("arguments[0].click();",add_note)
            time.sleep(2)
            added=driver.find_element(by=By.CSS_SELECTOR,value="textarea[name='message']")
            added.send_keys("hy welcome ,how are you")

            time.sleep(2)
            send=driver.find_element(by=By.XPATH,value="//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();",send)
            time.sleep(2)


    else:
        print("No URLs found in the CSV file.")
except FileNotFoundError:
    print(f"Error: File '{csv_file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(20)




