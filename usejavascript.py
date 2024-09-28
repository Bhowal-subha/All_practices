import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()


# To run in headless mode
option.add_argument("headless")
# To handle SSL certificate errors
option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=option)

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollBy(0,900)")
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# driver.get_screenshot_as_png()
driver.get_screenshot_as_file("abcd.png")

time.sleep(4)
