from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(8)
driver.maximize_window()
sign_in_popup = driver.find_element(By.XPATH, "//div[@class='sc-dcJsrY cjcrGc']")
close_popup = driver.find_element(By.XPATH, "//*[@class='sc-esYiGF khacGO']/div/div[2]/span")
close_popup.click()
alert_popup = driver.find_element(By.XPATH, "//p[@class='sc-jlwm9r-1 ewETUe']")
alert_popup.click()
driver.find_element(By.XPATH, "//div[@class='sc-12foipm-22 kGtxGm']/div").click()
from_destination = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
from_destination.send_keys("Sili")
list_of_destination = WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[@role='presentation']")))
for item1 in list_of_destination:
    airport_name = item1.find_element(By.XPATH, "div/div/div/p/span")
    # print(airport_name.text)
    if "Bagdogra" in airport_name.text:
        item1.click()
        break
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='sc-12foipm-22 OmQvV']").click()
to_destination = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
to_destination.send_keys("Benga")
list_of_destination2 = WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//ul/li[@role='presentation']")))
for item2 in list_of_destination2:
    destination_airport = WebDriverWait(item2, 5).until(
        EC.visibility_of_element_located((By.XPATH, "div/div/div/p/span")))
    # print(destination_airport.text)
    des_text=destination_airport.text
    if "Bengaluru" in des_text:
        item2.click()
        break
time.sleep(3)
# date = driver.find_element(By.XPATH, "//div[@class='sc-12foipm-0 iiZOql']/div[3]")
# date.click()
driver.quit()

