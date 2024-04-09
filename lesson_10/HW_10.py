import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': f'{os.getcwd()}\\downloads'
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

№1
driver.get('https://demoqa.com/upload-download')
upload_field = driver.find_element('xpath', '//input[@type="file"]')
upload_field.send_keys(f'{os.getcwd()}\\downloads\\img1.png')

time.sleep(3)

№2
driver.get('https://the-internet.herokuapp.com/download')
files = driver.find_elements('xpath', '(//div[@class="example"]//a)')
for file in files:
    file.click()
    print(file.text)