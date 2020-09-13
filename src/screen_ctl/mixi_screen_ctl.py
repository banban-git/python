from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

#ドライバー
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://mixi.jp/")

#E-mail入力
search_box = driver.find_element_by_name("email")
search_box.send_keys("testAAAAA")
#パスワード入力
search_box = driver.find_element_by_name("password")
search_box.send_keys("password")
time.sleep(0.5)

#ログイン
search_btn = driver.find_element_by_class_name("PORTAL_loginForm__button--gold")
search_btn.click()

time.sleep(3)

#スクリーンショット
screen = pyautogui.screenshot()
screen.save("スクリーンショット.png")