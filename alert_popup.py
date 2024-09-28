import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Example URL with alert
url = "https://rahulshettyacademy.com/AutomationPractice/"

# Open the URL
driver.get(url)

try:
    # Locate and click the button to trigger the alert
    alert_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,"alertbtn"))
    )
    alert_button.click()

    # Wait for the alert to appear
    #alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    # Print the text of the alert
    print("Alert text:", alert.text)
    time.sleep(5)
    # Accept the alert (click OK)
    alert.accept()

    # Optional: You can also dismiss the alert (click Cancel) using alert.dismiss()
    another_alert=driver.find_element(By.ID,"confirmbtn")

    another_alert.click()

    time.sleep(2)
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()

except Exception as e:
    print("Exception:", e)

finally:
    # Close the browser session
    driver.quit()
