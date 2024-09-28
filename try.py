
import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import service
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service_obj = Service("need to give driver path")
# driver = webdriver.Chrome(service=service_obj)
def driver():
    my_driver = webdriver.Chrome()
    my_driver.get("https://rahulshettyacademy.com/client/")
    time.sleep(3)
    my_driver.maximize_window()
    register_button = my_driver.find_element(By.CLASS_NAME, "btn1")
    register_button.click()
    time.sleep(2)
    first_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
    first_name.send_keys("Bobo")
    time.sleep(2)
    last_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
    last_name.send_keys("Biswas")
    time.sleep(2)
    email = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.ID, "userEmail")))
    email.send_keys("bobo3biswas@gmail.com")
    time.sleep(2)
    phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userMobile"]')))
    phone.send_keys("1234567891")
    time.sleep(2)
    occupation = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    'body > app-root > app-register > div.banner > section:nth-child(2) > div > div.login-wrapper.my-auto.p-5 > form > div:nth-child(3) > div:nth-child(1) > select')))
    select_0bj = Select(occupation)
    select_0bj.select_by_visible_text("Engineer")
    time.sleep(2)
    gender = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Male']")))
    gender.click()
    time.sleep(2)
    password = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='userPassword']")))
    password.send_keys("Bobo2345678")
    time.sleep(2)
    confirm_password = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='confirmPassword']")))
    confirm_password.send_keys("Bobo2345678")
    time.sleep(2)
    check_box = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    check_box.click()
    time.sleep(2)
    regi = my_driver.find_element(By.XPATH, '//input[@value="Register"]')
    regi.click()
    time.sleep(2)


driver()
