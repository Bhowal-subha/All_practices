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

try:
    table = driver.find_element(By.XPATH, "//table[@class='table-display']")

    # Find all rows in the table body
    rows = table.find_elements(By.XPATH, "tbody/tr")

    row_index = 4  # 5th row
    columns = table.find_elements(By.XPATH, f"tbody/tr[{row_index+1}]/td")  # Adding 1 to row_index for XPath

    # Check if there are enough columns
    if len(columns) >= 3:  # Ensure at least 3 columns (indexes 0, 1, 2 for columns 1, 2, 3 respectively)
        column2_value = columns[1].text  # Value from column 2
        column3_value = columns[2].text  # Value from column 3

        print(f"Value in column 2: {column2_value}")
        print(f"Value in column 3: {column3_value}")
# except Exception as e:
#     print(e)
finally:
    # refresh the WebDriver session
    driver.forward()
try:
    # Print headers
    headers = table.find_elements(By.XPATH,"tbody/tr[1]/th")
    print(f"{headers[0].text}\t\t{headers[1].text}\t\t{headers[2].text}")

    # Iterate through each row and print data
    for row in rows:
        # Find columns (country and capital)
        columns = row.find_elements(By.TAG_NAME,"td")
        if len(columns) >= 2:  # Ensure there are at least 2 columns
            country = columns[0].get_attribute("innerText")
            capital = columns[1].text
            print(f"{country}\t\t{capital}")

finally:
    # Close the WebDriver session
    driver.quit()
