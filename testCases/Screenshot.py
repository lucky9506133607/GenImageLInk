import time

import cloudinary
import cloudinary.uploader
import cloudinary.api
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Cloudinary credentials (replace these with your credentials)
cloudinary.config(
    cloud_name="du5exig8b",  # Replace with your Cloudinary Cloud Name
    api_key="276856828912681",        # Replace with your Cloudinary API Key
    api_secret="XqgsqnD_XyLm1knyl1h-jGQKeCk"   # Replace with your Cloudinary API Secret
)

# === 1. Take screenshot using Selenium ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pagespeed.web.dev/")
driver.fullscreen_window()
driver.find_element(By.XPATH, "//*[@id='i2']").send_keys("https://www.e2msolutions.com/")
driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div[2]/div/div[2]/form/div[2]/button").click()
print("Current URL:", driver.current_url)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="desktop_tab"]').click()
time.sleep(10)
print("Current URL:", driver.current_url)

screenshot_file = "..\\Assets\\E2MScreenshot.png"
driver.save_screenshot(screenshot_file)
driver.quit()

# === 2. Upload the screenshot to Cloudinary ===
response = cloudinary.uploader.upload(screenshot_file)

# === 3. Get the URL of the uploaded image ===
if 'secure_url' in response:
    print("✅ Screenshot uploaded successfully!")
    print("🌐 Access it here:", response['secure_url'])
else:
    print("❌ Upload failed:", response)
