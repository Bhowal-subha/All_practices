
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

file_path = r"C:\Users\subhowal\Downloads\download.xlsx"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.find_element(By.ID, "downloadButton").click()
# edit the Excel with updated value
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)
# wait = WebDriverWait(driver, 10)
toast_locator =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")))
toast_text = toast_locator.text
print(toast_text)
