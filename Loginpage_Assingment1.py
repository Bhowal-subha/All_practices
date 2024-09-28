import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, "blinkingText").click()

new_window = driver.window_handles
driver.switch_to.window(new_window[1])
get_email = driver.find_element(By.XPATH, "//strong/a").text
print(get_email)

driver.switch_to.window(new_window[0])
driver.find_element(By.ID, "username").send_keys(get_email)
driver.find_element(By.ID, "password").send_keys('123456')
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='form-check-inline']/label[2]/span[2]").click()

popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-body p")))
print(popup.text)

assert "You will be limited to only fewer functionalities of the app. Proceed?" == popup.text
driver.find_element(By.ID, "okayBtn").click()

seletc_option = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
seletc_option.select_by_visible_text("Consultant")

driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

wait = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(wait.text)
