import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
name_element.send_keys("Denny")

email_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
email_element.send_keys("abcd@gmail.com")

password_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "exampleInputPassword1")))
password_element.send_keys("123456")

mark_checkbox = driver.find_element(By.ID, "exampleCheck1")
mark_checkbox.click()

time.sleep(3)

gender_element = driver.find_element(By.ID, "exampleFormControlSelect1")
# handle the dropdown using Keys class
# gender_element.click()
# gender_element.send_keys(Keys.ENTER)

# another way to handle dropdown using select(static)
select_option = Select(gender_element)
select_option.select_by_visible_text("Female")

employement_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inlineRadio2")))
employement_status.click()

date_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='bday']")))
date_option.send_keys("04-02-1996")

click_submit = driver.find_element(By.CLASS_NAME, "btn")
click_submit.click()

get_text = driver.find_element(By.CLASS_NAME, "alert-success")
original_text = get_text.text
print(original_text)

assert "Success" in original_text

time.sleep(5)
