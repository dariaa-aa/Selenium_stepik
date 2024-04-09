import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get('https://demoqa.com/dynamic-properties')

# visible_after_button = ('xpath', '//button[@id="visibleAfter"]')
# wait.until(EC.visibility_of_element_located(visible_after_button)).click()

# enable_in_seconds_button = ('xpath', '//button[@id="enableAfter"]')
# wait.until(EC.element_to_be_clickable(enable_in_seconds_button)).click()

driver.get('https://the-internet.herokuapp.com/dynamic_controls')

# remove_button = ('xpath', '//button[text()="Remove"]')
# driver.find_element(*remove_button).click()
#
# wait.until(EC.invisibility_of_element_located(remove_button))
#
# print("it's okey")

enable_button = ('xpath', '//button[text()="Enable"]')
text_field = ('xpath', '//input[@type="text"]')

wait.until(EC.element_to_be_clickable(enable_button)).click()
wait.until(EC.element_to_be_clickable(text_field)).send_keys('HELLO')
wait.until(EC.text_to_be_present_in_element_value(text_field, 'HELLO'))

print("it's ok")