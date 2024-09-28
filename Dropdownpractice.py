import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

# Handle dynamic dropdown box
country_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "autosuggest")))
country_element.send_keys("ind")
time.sleep(2)

select_option = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

for option in select_option:
    if option.text == "India":
        option.click()
        break
time.sleep(3)
