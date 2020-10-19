# ocr_card.py
import pyautogui
import time
import os
from PIL import Image
import pyocr
import pyocr.builders
import cv2
import re
import imagehash

#環境設定
TESSERACT_PATH= "C:\\Program Files\\Tesseract-OCR"
# 1.インストール済みのTesseractのパスを通す
path_tesseract = TESSERACT_PATH
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# ---------------------
# メイン関数
# ---------------------
def main():
    time.sleep(3)
    #ゲームスタート
    pyautogui.press('enter')
    time.sleep(2)
    isFirst = True

    while True:
        sc = pyautogui.screenshot(region=(500, 460, 340, 25))
        sc.save('SushidaPicture.jpg')
        img = cv2.imread('SushidaPicture.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        tmp = cv2.resize(gray, (gray.shape[1]*2, gray.shape[0]*2), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite('SushidaPicture.jpg', tmp)
        if isFirst:
            cv2.imwrite('SushidaPicture2.jpg', tmp)
            isFirst = False
        
        # 入力文字取得
        sushidaMoji = get_sushida_moji("C:/work/python/SushidaPicture.jpg")
        # エラーの場合
        if is_sushida_input_error():
            # 再度読み込み
            sushidaMoji = get_sushida_moji("C:/work/python/SushidaPicture2.jpg")
            
        # 文字入力
        print(sushidaMoji)
        pyautogui.write(sushidaMoji, interval=0.00000001)
        # 文字入力
        cv2.imwrite('SushidaPicture2.jpg', tmp)

# --------------------------------------
# 寿司打入力エラー
# @return true:エラーあり、false:エラーなし
# --------------------------------------
def is_sushida_input_error():
    # 前回の画像と比較して、同じ画像（ハッシュ値）の場合はtrueを返却する。
    hash1= imagehash.average_hash(Image.open("C:/work/python/SushidaPicture.jpg"))
    hash2 = imagehash.average_hash(Image.open("C:/work/python/SushidaPicture2.jpg"))
    return hash1 == hash2

# ---------------------
# 入力文字取得
# ---------------------
def get_sushida_moji(imgFileDir):
    # 画像読み込み
    img_org = Image.open(imgFileDir)
    # 文字取得
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(img_org, lang="eng", builder=builder)
    # 前後空白除去
    sushidaMoji = re.sub('^.{6} + ', '', result)
    sushidaMoji = re.sub(' +.*', '', sushidaMoji)
    # 全て小文字に変更
    sushidaMoji = sushidaMoji.lower()
    return sushidaMoji

# ---------------------
# メイン関数
# ---------------------
if __name__ == "__main__":
    main()