from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
browser.get("https://covid19.who.int/WHO-COVID-19-global-data.csv")
time.sleep(3)