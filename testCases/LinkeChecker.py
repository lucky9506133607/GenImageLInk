import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Record_Video import Desktop_Recording
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Screenshot import Screenshot

# === 1. Take screenshot using Selenium ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.drlinkcheck.com/")
driver.fullscreen_window()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='url']").send_keys("https://www.e2msolutions.com/")
driver.find_element(By.XPATH,"//div[@class='container']//div[@class='btn btn-default'][normalize-space()='Start Check']").click()
print("Current URL:", driver.current_url)

# Wait for the results to load by waiting for a specific element that appears after analysis
try:
    # Wait up to 60 seconds for the results element to appear (adjust selector as needed)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='table-progress']"))
    )
    print("Dr link Checker Overview loaded!")
except Exception as e:
    print("Timed out waiting for results to load:", e)

print("Current URL:", driver.current_url)

time.sleep(1)
recording = Desktop_Recording() #Recording class call

def wait_for_progress_to_finish(driver, timeout=120):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.find_elements(By.XPATH, "//div[@class='table-progress']")) == 0
        )
        print("Progress finished, attribute is gone!")
    except TimeoutException:
        print("Timed out waiting for progress to finish.")

wait_for_progress_to_finish(driver)
recording.Record(driver)  # pass the driver you already have open

capture = Screenshot()
capture.capture_screenshot(driver, "LinkChecker_Overview")
driver.quit()





