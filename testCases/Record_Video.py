class Desktop_Recording:
    def Record(self, driver, output_file="../Assets/E2M.mp4"):
        import cv2
        import numpy as np
        import time
        import mss

        monitor = {
            "top": 0,
            "left": 0,
            "width": 1920,
            "height": 1080
        }
        fps = 15
        SCROLL_SPEED = 30
        SCROLL_DELAY = 0.1

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_writer = cv2.VideoWriter(output_file, fourcc, fps, (monitor["width"], monitor["height"]))

        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_y = 0

        with mss.mss() as sct:
            while scroll_y < total_height:
                driver.execute_script(f"window.scrollTo(0, {scroll_y})")
                time.sleep(SCROLL_DELAY)
                frame = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                video_writer.write(frame)
                scroll_y += SCROLL_SPEED
                print(f"\r📸 Scrolled to: {scroll_y}px", end="", flush=True)

        video_writer.release()
        print("✅ Recording complete:", output_file)