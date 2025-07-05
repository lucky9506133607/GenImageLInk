import time

import cloudinary
import cloudinary.uploader
import cloudinary.api
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# === 1. Take screenshot using Selenium ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://pagespeed.web.dev/")
driver.get("https://www.drlinkcheck.com/")
driver.fullscreen_window()
driver.find_element(By.XPATH, "//*[@id='url']").send_keys("https://www.e2msolutions.com/")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div").click()
print("Current URL:", driver.current_url)
time.sleep(5)
#driver.find_element(By.XPATH, '//*[@id="desktop_tab"]').click()
driver(driver, 30).until(lambda d: d.execute_script("return document.readyState") == "complete")
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
