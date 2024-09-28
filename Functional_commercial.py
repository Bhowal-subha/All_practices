import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, 'input[type=search]').send_keys('ber')
time.sleep(2)
add_to_cart = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
for add in add_to_cart:
    add.click()

accutal_list = []
item_names = driver.find_elements(By.XPATH, "//div[@class='product']")
for item in item_names:
    accutal_list.append(item.find_element(By.XPATH, "h4").text)
print(accutal_list)

take_item_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h4[class='product-name']")))

driver.find_element(By.XPATH, "//*[@id='root']/div/header/div/div[3]/a[4]/img").click()
cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
cart.click()

# time.sleep(2)
# current_url = driver.current_url
# assert current_url == 'https://rahulshettyacademy.com/seleniumPractise/#/cart'

sum = 0
product_amaount = driver.find_elements(By.XPATH, "//tr/td[5]/p")
for price in product_amaount:
    sum += int(price.text)
total_amaount = driver.find_element(By.XPATH, "//span[@class='totAmt']")

assert sum == int(total_amaount.text)

driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
promo_info = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
assert promo_info.is_displayed()

amaount_after_dis = driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']")

assert float(amaount_after_dis.text) < int(total_amaount.text)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

country_select = Select(driver.find_element(By.XPATH, "//select"))
country_select.select_by_visible_text("India")

driver.find_element(By.XPATH, "//input[@class='chkAgree']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button").click()

time.sleep(5)
