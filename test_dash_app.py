from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver path
chromedriver_path = r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
chrome_path = r"C:\chrome-win64\chrome-win64\chrome.exe"

# Set Chrome options
options = Options()
options.binary_location = chrome_path
options.add_argument("--start-maximized")  # optional
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start ChromeDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open a website (example: Google)
driver.get("https://www.google.com")

time.sleep(5)  # wait to see the browser

print("Page Title:", driver.title)

driver.quit()
