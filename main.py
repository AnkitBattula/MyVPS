from keep_alive import keep_alive
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com/watch?v=fSu1qqkX13A&list=PL-IjflSUTbwNnJ9hKl9SdeZaiMPWTsbbX")

keep_alive()