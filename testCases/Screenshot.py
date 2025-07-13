import time

import cloudinary
import cloudinary.uploader
import cloudinary.api
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from html2image import Html2Image
import base64



cloudinary.config(
    cloud_name="du5exig8b",  # Replace with your Cloudinary Cloud Name
    api_key="276856828912681",        # Replace with your Cloudinary API Key
    api_secret="XqgsqnD_XyLm1knyl1h-jGQKeCk"   # Replace with your Cloudinary API Secret
)

class Screenshot:
    def capture_screenshot(self, driver, site_ss):
        screenshot_file = "..\\Assets\\"+site_ss+".png"
        width = 1920
        height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        driver.set_window_size(width, height)
        driver.find_element(By.TAG_NAME, "body").screenshot(screenshot_file)
        #response = cloudinary.uploader.upload(screenshot_file)
        #print("cloudinary = ", response)
        # === 3. Get the URL of the uploaded image ===
        """if response:
            print("✅ Screenshot uploaded successfully!")
            print("🌐 Access it here:", response['E2MScreenshot'])
        else:
            print("❌ Upload failed:", response)"""

