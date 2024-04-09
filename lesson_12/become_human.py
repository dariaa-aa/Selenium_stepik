import time
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
options.add_argument('--headless')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# driver.get('https://dzen.ru')
# driver.save_screenshot('screen.png')

# driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

driver.get('https://whatismyipaddress.com/')
driver.save_screenshot('12.png')
wait.until(EC.title_is('What Is My IP Address - See Your Public Address - IPv4 & IPv6'))
# time.sleep(5)