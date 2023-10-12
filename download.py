from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.get("https://covid19.who.int/WHO-COVID-19-global-data.csv")
time.sleep(3)