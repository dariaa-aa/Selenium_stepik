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

# driver.get('https://the-internet.herokuapp.com/checkboxes')
#
# checkbox_1 = ('xpath','(//input[@type="checkbox"])[1]')
# print(driver.find_element(*checkbox_1).get_attribute('checked'))
# driver.find_element(*checkbox_1).click()
# print(driver.find_element(*checkbox_1).get_attribute('checked'))
# # assert driver.find_element(*checkbox_1).get_attribute('checked') is not None
# assert driver.find_element(*checkbox_1).is_selected()

# driver.get('https://demoqa.com/checkbox')
# checkbox_home_status = ('xpath', '//input[@id="tree-node-home"]')
# checkbox_home_action = ('xpath', '//span[@class="rct-checkbox"]')
# print(driver.find_element(*checkbox_home_status).is_selected())
# driver.find_element(*checkbox_home_action).click()
# print(driver.find_element(*checkbox_home_status).is_selected())

# driver.get('https://demoqa.com/selectable')
# element_1 = ('xpath', '//li[text()="Cras justo odio"]')
# before = driver.find_element(*element_1).get_attribute('class')
# print(before)
# driver.find_element(*element_1).click()
# after = driver.find_element(*element_1).get_attribute('class')
# print(after)
# assert 'active' in after

driver.get('https://demoqa.com/radio-button')
yes_radio_status = ('xpath', '//input[@id="yesRadio"]')
yes_radio_action = ('xpath', '//label[@for="yesRadio"]')
no_radio_status = ('xpath', '//input[@id="noRadio"]')
no_radio_action = ('xpath', '//label[@for="noRadio"]')

# before = driver.find_element(*yes_radio_status).is_selected()
# print(before)
# driver.find_element(*yes_radio_action).click()
# after = driver.find_element(*yes_radio_status).is_selected()
# print(after)

print(driver.find_element(*no_radio_status).is_enabled())
print(driver.find_element(*yes_radio_status).is_enabled())