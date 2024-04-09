from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from csv import DictReader


driver=webdriver.Chrome()
driver.get('https://www.linkedin.com/')
time.sleep(4)

def get_cookies_values(file):
    with open(file, encoding='utf-8-sig') as f:
        dict_reader = DictReader(f)
        list_of_dicts=list(dict_reader)
    return list_of_dicts

time.sleep(4)

cookies=get_cookies_values("linkedin_cookie.csv")

time.sleep(4)

for i in cookies:
    driver.add_cookie(i)

time.sleep(4)
driver.refresh()
time.sleep(10)
driver.get("https://www.linkedin.com/search/results/people/?origin=CLUSTER_EXPANSION&sid=4XS")