import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

№1
change_text_button = ('xpath', '//button[@id="populate-text"]')
text = ('xpath', '//h2[@class="target-text"]')

driver.find_element(*change_text_button).click()
wait.until(EC.text_to_be_present_in_element(text, 'Selenium Webdriver'))

№2
display_button = ('xpath', '//button[@id="display-other-button"]')
enabled_button = ('xpath', '//button[@id="hidden"]')

driver.find_element(*display_button).click()
wait.until(EC.visibility_of_element_located(enabled_button))

№3
enable_button = ('xpath', '//button[@id="enable-button"]')
button_button = ('xpath', '//button[@id="disable"]')

driver.find_element(*enable_button).click()
wait.until(EC.element_to_be_clickable(button_button)).click()

№4
alert_button = ('xpath', '//button[@id="alert"]')

driver.find_element(*alert_button).click()
wait.until(EC.alert_is_present())

print("it's ok")


