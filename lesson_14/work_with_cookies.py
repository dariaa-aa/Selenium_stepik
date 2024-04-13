import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/en/us/login')

# print(driver.get_cookie('country_code'))
# print(driver.get_cookies())

# driver.add_cookie({
#     'name': 'Example',
#     'value': 'Kukushka'
# })
#
# print(driver.get_cookie('Example'))

# before = driver.get_cookie('split')
# print(before)
#
# driver.delete_cookie('split')
# driver.add_cookie({
#     'name': 'split',
#     'value': 'qwerty'
# })
#
# after = driver.get_cookie('split')
# print(after)

# before = driver.get_cookies()
# print(before)
#
# driver.delete_all_cookies()
#
# driver.add_cookie({
#     'name': 'split',
#     'value': 'qwerty'
# })
#
# after = driver.get_cookies()
# print(after)

# email_field = ('xpath', '(//input[contains(@class, "login_email")])[1]')
# password_field = ('xpath', '(//input[contains(@class, "form_pad")])[1]')
# sub_button = ('xpath', '//button[@id="loginformsubmit"]')
#
# driver.find_element(*email_field).send_keys('autocheck@ya.ru')
# driver.find_element(*password_field).send_keys('123')
# driver.find_element(*sub_button).click()
#
# pickle.dump(driver.get_cookies(), open(os.getcwd()+'\\cookies\\cookies.pkl', 'wb'))

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+'\\cookies\\cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)