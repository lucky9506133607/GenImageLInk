import cv2
import numpy as np
import time
import mss
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


monitor = {"top": 0, "left": 0, "width": 1280, "height": 720}

# Output video settings
output_file = "recorded_browser.mp4"
fps = 15

# Set up video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(output_file, fourcc, fps, (monitor["width"], monitor["height"]))


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1280, 720)
driver.set_window_position(0, 0)
driver.get("https://example.com")

# Start screen recording
with mss.mss() as sct:
    start_time = time.time()
    while True:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        video_writer.write(frame)

        # Stop after 10 seconds
        if time.time() - start_time > 10:
            break

## Cleanup
driver.quit()
video_writer.release()
print("✅ Recording complete: recorded_browser.mp4")