import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

№1
driver.get('https://demoqa.com/text-box')

username_field = driver.find_element('xpath', '//input[@id="userName"]')
email_field = driver.find_element('xpath', '//input[@id="userEmail"]')
curr_adress_field = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
perm_adress_field = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')

username_field.clear()
email_field.clear()
curr_adress_field.clear()
perm_adress_field.clear()

username_field.send_keys('Daria')
email_field.send_keys('dashapodolskaya@mail.ru')
curr_adress_field.send_keys('Tbilisi')
perm_adress_field.send_keys('Earth')

assert username_field.get_attribute('value') == 'Daria'
assert email_field.get_attribute('value') == 'dashapodolskaya@mail.ru'
assert curr_adress_field.get_attribute('value') == 'Tbilisi'
assert perm_adress_field.get_attribute('value') == 'Earth'

time.sleep(3)

№2
driver.get('https://the-internet.herokuapp.com/status_codes')

status_200 = driver.find_element('xpath', '//a[text()="200"]')
status_301 = driver.find_element('xpath', '//a[text()="301"]')
status_404 = driver.find_element('xpath', '//a[text()="404"]')
status_500 = driver.find_element('xpath', '//a[text()="500"]')

status_200.click()
time.sleep(3)
driver.back()
status_301.click()
time.sleep(3)
driver.back()
status_404.click()
time.sleep(3)
driver.back()
status_500.click()
time.sleep(3)
driver.back()

time.sleep(3)