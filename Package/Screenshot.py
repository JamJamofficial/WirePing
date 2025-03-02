import pyautogui

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("[+] Screenshot saved")

if __name__ == "__main__":
    take_screenshot()
