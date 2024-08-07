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

# Open the login page
driver.get(login_page_url)

# Wait for the cookie consent pop-up to be present
try:
    cookie_accept_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BRP_MODAL_CONTAINER"]/div[2]/div[2]/div/div/div[4]/div[1]/div[2]'))  # Update the XPath as needed
    )
    cookie_accept_button.click()
except TimeoutException:
    print("No cookie consent pop-up found or it took too long to load.")
    
# Wait for the login elements to be present
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BRP_MODAL_CONTAINER"]/div/div[2]/div/div[2]/div/form/div[2]/div/div[2]/input'))
    )
except TimeoutException:
    print("Login page elements took too long to load.")
    driver.quit()
    exit()
    
# Wait for the remember consent pop-up to be present
try:
    cookie_accept_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BRP_MODAL_CONTAINER"]/div/div[2]/div/div[2]/div/form/div[4]/div/div/div[1]'))  # Update the XPath as needed
    )
    cookie_accept_button.click()
except TimeoutException:
    print("No remember consent pop-up found or it took too long to load.")

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.XPATH, '//*[@id="BRP_MODAL_CONTAINER"]/div/div[2]/div/div[2]/div/form/div[2]/div/div[2]/input')
password_field = driver.find_element(By.XPATH, '//*[@id="BRP_MODAL_CONTAINER"]/div/div[2]/div/div[2]/div/form/div[3]/div/div[2]/div[1]/input')

username_field.send_keys("THE USERNAME")
password_field.send_keys("THE PASSWORD")
password_field.send_keys(Keys.RETURN)

time.sleep(2)
# Wait for login to complete by checking if redirected or if the target page is accessible
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "root"))
    )
except TimeoutException:
    print("Login might not be successful or page took too long to load.")
    print("Current URL:", driver.current_url)
    print("Page Source:", driver.page_source)
    driver.quit()
    exit()

# Navigate to the target page if not redirected automatically
driver.get(target_page_url)

# Wait for the content to load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "root"))
    )
except TimeoutException:
    print("Protected page content took too long to load or element not found.")
    print("Current URL:", driver.current_url)
    print("Page Source:", driver.page_source)
    driver.quit()
    exit()
time.sleep(1)

div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div/div[3]/div[3]')

print(div.text)

# Close the WebDriver
driver.quit()