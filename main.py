import cloudinary
import cloudinary.uploader
import cloudinary.api
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Cloudinary credentials (replace these with your credentials)
cloudinary.config(
    cloud_name="du5exig8b",  # Replace with your Cloudinary Cloud Name
    api_key="276856828912681",        # Replace with your Cloudinary API Key
    api_secret="XqgsqnD_XyLm1knyl1h-jGQKeCk"   # Replace with your Cloudinary API Secret
)

# === 1. Take screenshot using Selenium ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com")

screenshot_file = "screenshot.png"
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
