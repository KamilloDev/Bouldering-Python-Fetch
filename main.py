from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Define the login page URL and the target URL after login
login_page_url = "https://boulders.goactivebooking.com/login"
target_page_url = "https://boulders.goactivebooking.com/my-pages"