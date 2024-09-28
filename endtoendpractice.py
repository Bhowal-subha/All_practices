import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Shop']").click()

all_items=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for items in all_items:
    item=items.find_element(By.XPATH,"div[1]/h4/a")
    if item.text=="Blackberry":
        items.find_element(By.XPATH,"div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='navbarResponsive']/ul/li/a").click()
# driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
get_country=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
get_country.click()

time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

fetch_text=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
print(fetch_text.text)
assert "Success!" in fetch_text.text

time.sleep(3)
