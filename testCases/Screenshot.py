import time

import cloudinary
import cloudinary.uploader
import cloudinary.api
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

cloudinary.config(
    cloud_name="du5exig8b",  # Replace with your Cloudinary Cloud Name
    api_key="276856828912681",        # Replace with your Cloudinary API Key
    api_secret="XqgsqnD_XyLm1knyl1h-jGQKeCk"   # Replace with your Cloudinary API Secret
)

class Screenshot:
    def capture_screenshot(self, driver):
        screenshot_file = "..\\Assets\\E2MScreenshot.png"
        # Get the total height of the page
        total_height = driver.execute_script("return document.body.scrollHeight")
        total_width = driver.execute_script("return document.body.scrollWidth")

        # Set window size to capture full page
        driver.set_window_size(total_width, total_height)
        driver.save_screenshot(screenshot_file)
        response = cloudinary.uploader.upload(screenshot_file)
        print("cloudinary = ", response)
        # === 3. Get the URL of the uploaded image ===
        if response == True:
            print("✅ Screenshot uploaded successfully!")
            print("🌐 Access it here:", response['E2MScreenshot'])
        else:
            print("❌ Upload failed:", response)

