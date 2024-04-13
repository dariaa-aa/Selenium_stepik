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
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.ge

№1
cookie_1 = {
    'name': 'username',
    'value': 'user123'
}

driver.add_cookie(cookie_1)
driver.refresh()
time.sleep(15)
assert driver.get_cookie('username')['value'] == 'user123'
print(driver.get_cookie('username')['value'])

№2
driver.delete_cookie('zen_vk_gid')
driver.refresh()
assert driver.get_cookie('zen_vk_gid') == None

№3t('https://dzen.ru/')
driver.get('https://www.amazon.com/')
time.sleep(13)
driver.find_element('xpath', '//span[text()="Health and Beauty"]').click()
driver.find_element('xpath', '//span[contains(text(), "Dove Exfoliating")]').click()
driver.find_element('xpath', '//input[@id="add-to-cart-button"]').click()
pickle.dump(driver.get_cookies(), open(f'{os.getcwd()}\\cookies\\HW_cookies.pkl', 'wb'))
driver.delete_all_cookies()
driver.refresh()
cookies = pickle.load(open(f'{os.getcwd()}\\cookies\\HW_cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)