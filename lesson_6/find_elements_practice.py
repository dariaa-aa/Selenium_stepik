import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://hyperskill.org/tracks')

time.sleep(3)

# print(driver.find_elements('class name', 'nav-link'))
# print(len(driver.find_elements('class name', 'nav-link')))
elements = driver.find_elements('class name', 'nav-link')
for element in elements:
    print(element.text)

# driver.find_elements('class name', 'nav-link')[3].click()

# time.sleep(5)