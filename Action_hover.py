import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(2)
driver.execute_script("window.scrollBy(300,900)")
time.sleep(1)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(2)

action.move_by_offset(400, 600)
# action.drag_and_drop(source,target)

time.sleep(2)
driver.find_element(By.LINK_TEXT, "Top").click()


