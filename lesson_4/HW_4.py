import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url_1 = 'https://vk.com/'
url_2 = 'https://ya.ru/'

driver.get(url_1)

current_title_1 = driver.title
print('Текущий заголовок:', current_title_1)

driver.get(url_2)

current_title_2 = driver.title
print('Текущий заголовок:', current_title_2)

driver.back()

assert driver.title == current_title_1, 'Мы все еще в Яндексе'

driver.refresh()

current_url = driver.current_url
print('Текущий URL:', current_url)

driver.forward()

current_url = driver.current_url

assert current_url == url_2, 'Мы в ВК'