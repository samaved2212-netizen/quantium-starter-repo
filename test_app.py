from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Paths
chrome_driver_path = r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
chrome_binary_path = r"C:\chrome-win64\chrome-win64\chrome.exe"

# Set up Chrome service
service = Service(executable_path=chrome_driver_path)

# Set Chrome options
options = Options()
options.binary_location = chrome_binary_path  # Use your Chrome binary
options.add_argument("--start-maximized")      # Start Chrome maximized
# options.add_argument("--headless")           # Uncomment for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open Google to test
driver.get("https://www.google.com")

# Print page title
print("Page Title:", driver.title)

# Wait 5 seconds before closing
time.sleep(5)
driver.quit()
