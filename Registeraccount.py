import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(2)

find_register_ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
find_register_ele.click()
time.sleep(3)

current_url = driver.current_url
print(current_url)
assert current_url == "https://rahulshettyacademy.com/client/auth/register"

fname_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
fname_element.send_keys("Jhon")

lname_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
lname_element.send_keys("The Don")

email_element = driver.find_element(By.ID, "userEmail")
email_element.send_keys("jhontheg@gmail.com")
time.sleep(3)

phone_element = driver.find_element(By.ID, "userMobile")
phone_element.send_keys("9999999999")

occupation_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/app-root/app-register/div[1]/section[2]/div/div[2]/form/div[3]/div[1]/select")))
select_element = Select(occupation_element)
select_element.select_by_visible_text("Engineer")
time.sleep(2)

gender_element=driver.find_element(By.XPATH,"//input[@value='Male']")
gender_element.click()

password_element=driver.find_element(By.ID,"userPassword")
password_element.send_keys("Jhonthedon1")

conf_password_element=driver.find_element(By.ID,"confirmPassword")
conf_password_element.send_keys("Jhonthedon1")

required_box=driver.find_element(By.XPATH,"//input[@formcontrolname='required']")
required_box.click()
time.sleep(2)

driver.find_element(By.ID,"login").click()
time.sleep(2)

successful_message=driver.find_element(By.CLASS_NAME,'headcolor').text
print(successful_message)
assert  "Successfully" in successful_message
time.sleep(2)