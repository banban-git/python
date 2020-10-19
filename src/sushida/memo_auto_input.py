import pyautogui
import time

# メモ帳を開く
pyautogui.press('win')
pyautogui.write('note')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

# 文字入力
pyautogui.write('Hello World', interval=0.1)
pyautogui.keyDown('ctrl')
pyautogui.press(['a', 'c'])
pyautogui.keyUp('ctrl')
# コピーした文字列を張り付ける
for num in range(2):
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
# 中身を消去
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')

# メモ帳の終了
pyautogui.hotkey('alt', 'f4')