import cv2
import numpy as np
import time
import mss
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


monitor = {
    "top": 0,
    "left": 0,
    "width": 1920,
    "height": 1080
}

# Output video settings
output_file = "E2M.mp4"
SCROLL_SPEED   = 30                     # pixels per step
SCROLL_DELAY   = 0.1                    # seconds between scroll steps
RESOLUTION     = (1920, 1080)            # browser window size
fps = 15                                # frame rate for output video

# Set up video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (monitor["width"], monitor["height"]))


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(*RESOLUTION)
driver.set_window_position(0, 0)
driver.get("https://www.e2msolutions.com/")
driver.fullscreen_window()
total_height = driver.execute_script("return document.body.scrollHeight")
print(f"🌐 Page height: {total_height}px")

# Setup video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(
    output_file, fourcc, fps, (monitor["width"], monitor["height"])
    )

with mss.mss() as sct:
    try:
        scroll_y = 0
        while scroll_y < total_height:
            # Scroll to position
            driver.execute_script(f"window.scrollTo(0, {scroll_y})")
            time.sleep(SCROLL_DELAY)

            # Capture current screen
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            video_writer.write(frame)

            # Move to next scroll step
            scroll_y += SCROLL_SPEED
            print(f"\r📸 Scrolled to: {scroll_y}px", end="", flush=True)

        print("\n✅ Full-page recording completed.")

    finally:
        video_writer.release()
        driver.quit()
print("✅ Recording complete: recorded_browser.mp4")

