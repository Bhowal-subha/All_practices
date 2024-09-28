from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

item_list=[]
items=driver.find_elements(By.XPATH,"//tr/td[1]")
for item in items:
    item_list.append(item.text)

browser_items=item_list

item_list.sort()

assert item_list==browser_items

