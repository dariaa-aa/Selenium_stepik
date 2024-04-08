import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://testautomationpractice.blogspot.com/')

# driver.find_element('class name', 'wikipedia-icon').click()
# driver.find_element('id', 'Wikipedia1_wikipedia-search-input').click()
# driver.find_element('class name', 'wikipedia-search-button').click()

driver.find_elements('tag name', 'button')[0].click()

time.sleep(5)