import pyautogui
import time
import os
from PIL import Image
import pyocr
import pyocr.builders
import cv2
import re
import imagehash

# リン打
# https://typing.twi1.me/game/5190

#ゲームスタート
time.sleep(3)
pyautogui.press('space')
time.sleep(2)

while True:            
    # 文字入力
    pyautogui.write("rinn", interval=0)
    