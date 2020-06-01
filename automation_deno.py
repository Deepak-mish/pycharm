from PIL import Image, ImageGrab
import pyautogui
import time


def screenshot():
    img = ImageGrab.grab().convert('L')
    return img


def press(key):
    pyautogui.keyDown(key)
    return


# x=566, y=393
# x=465, y=436
def detect(data):
    for i in range(393, 556):
        for j in range(436, 465):
            if data[i, j] < 100:
                press('up')
                return


press('up')
time.sleep(2)

while True:
    img = screenshot()
    data = img.load()
    detect(data)
