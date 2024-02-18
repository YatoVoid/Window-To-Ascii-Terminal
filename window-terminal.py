import os
import time
import pygetwindow as gw
import pyautogui
from PIL import Image

def capture_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        rect = (window.left, window.top, window.width, window.height)
        screenshot = pyautogui.screenshot(region=rect)
        return screenshot
    except IndexError:
        print(f"Window with title '{window_title}' not found.")
        window_title = input("Window Title:")
        return None

def convert_to_ascii(image, width=100):
    image = image.resize((width, int(width * image.size[1] / image.size[0])))
    ascii_chars = "@%#*+=-:. "
    pixels = image.convert("L").getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[min(pixel_value * len(ascii_chars) // 256, len(ascii_chars)-1)]
    return ascii_str

def display_ascii_image(ascii_image, width):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(0, len(ascii_image), width):
        print(ascii_image[i:i+width])

if __name__ == "__main__":

    window_title = "Window Title"
    window_title = input("Window Title:")
    ascii_width = 125

    while True:
        captured_image = capture_window(window_title)
        if captured_image:
            ascii_image = convert_to_ascii(captured_image, width=ascii_width)
            display_ascii_image(ascii_image, ascii_width)
