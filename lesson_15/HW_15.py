import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--window-size=1920,1080')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/selectable')
driver.find_element('xpath', '//a[@id="demo-tab-grid"]').click()
checkbox_one_action = ('xpath', '//li[text()="One"]')
checkbox_one_status = ('xpath', '(//div[@id="row1"]/li)[1]')

before = driver.find_element(*checkbox_one_status).get_attribute('class')
print(before)
driver.find_element(*checkbox_one_action).click()
after = driver.find_element(*checkbox_one_status).get_attribute('class')
print(after)
assert 'active' in after


checkbox_two_action = ('xpath', '//li[text()="Five"]')
checkbox_two_status = ('xpath', '(//div[@id="row2"]/li)[2]')

before_2 = driver.find_element(*checkbox_two_status).get_attribute('class')
print(before_2)
driver.find_element(*checkbox_two_action).click()
after_2 = driver.find_element(*checkbox_two_status).get_attribute('class')
print(after_2)
assert 'active' in after_2

driver.find_element(*checkbox_one_action).click()
driver.find_element(*checkbox_two_action).click()
assert 'active' not in driver.find_element(*checkbox_one_status).get_attribute('class')
assert 'active' not in driver.find_element(*checkbox_two_status).get_attribute('class')