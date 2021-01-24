from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)
# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(executable_path="/Users/vincenthsieh/Downloads/chromedriver")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file

# function to handle setting up headless download
download_dir = "/Users/vincenthsieh/covid_dash"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)
# get request to target the site selenium is active on
driver.get("https://covid19.who.int/WHO-COVID-19-global-data.csv")
time.sleep(3)