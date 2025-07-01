from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = r"C:\Users\Admin\PowerLearnProject\AI for Software Engineering\AI in software engineering\task 2\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# Load the local mock login page
driver.get("file:///C:/Users/Admin/PowerLearnProject/AI%20for%20Software%20Engineering/AI%20in%20software%20engineering/task%202/mock_login.html")

def login(username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginButton").click()
    # Wait for the message div to update
    time.sleep(1)  # Allow time for JS message to appear

# Test 1: Valid credentials
login("admin", "1234")
message = driver.find_element(By.ID, "message").text
if "Welcome" in message:
    print("✅ Valid Login Passed")
else:
    print("❌ Valid Login Failed")

# Test 2: Invalid credentials
driver.get("file:///C:/Users/Admin/PowerLearnProject/AI%20for%20Software%20Engineering/AI%20in%20software%20engineering/task%202/mock_login.html")
login("admin", "wrongpass")
message = driver.find_element(By.ID, "message").text
if "Invalid" in message:
    print("✅ Invalid Login Detected")
else:
    print("❌ Invalid Login Not Handled")

driver.quit()
