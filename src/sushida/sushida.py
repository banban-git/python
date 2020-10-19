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

# 寿司打 http://typingx0.net/sushida/play.html

# 現在のイメージファイル
NOW_IMAGE_SUSHIDA_FILE= "now_SushidaPicture.jpg"
# 前回のイメージファイル
PREVIOUS_IMAGE_SUSHIDA_FILE= "previous_SushidaPicture.jpg"

#環境設定
TESSERACT_PATH= "C:\\Program Files\\Tesseract-OCRetu"
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
        sc.save(NOW_IMAGE_SUSHIDA_FILE)
        img = cv2.imread(NOW_IMAGE_SUSHIDA_FILE)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        tmp = cv2.resize(gray, (gray.shape[1]*2, gray.shape[0]*2), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(NOW_IMAGE_SUSHIDA_FILE, tmp)
        if isFirst:
            cv2.imwrite(PREVIOUS_IMAGE_SUSHIDA_FILE, tmp)
            isFirst = False
        
        # 入力文字取得
        sushidaMoji = get_sushida_moji("C:/work/python/" + NOW_IMAGE_SUSHIDA_FILE)
        # エラーの場合
        if is_sushida_input_error():
            # 再度読み込み
            sushidaMoji = get_sushida_moji("C:/work/python/" + PREVIOUS_IMAGE_SUSHIDA_FILE)
            
        # 文字入力
        print(sushidaMoji)
        pyautogui.write(sushidaMoji, interval=0.00000001)
        # 文字入力
        cv2.imwrite(PREVIOUS_IMAGE_SUSHIDA_FILE, tmp)

# --------------------------------------
# 寿司打入力エラー
# @return true:エラーあり、false:エラーなし
# --------------------------------------
def is_sushida_input_error():
    # 前回の画像と比較して、同じ画像（ハッシュ値）の場合はtrueを返却する。
    hash1= imagehash.average_hash(Image.open("C:/work/python/" + NOW_IMAGE_SUSHIDA_FILE))
    hash2 = imagehash.average_hash(Image.open("C:/work/python/" + PREVIOUS_IMAGE_SUSHIDA_FILE))
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