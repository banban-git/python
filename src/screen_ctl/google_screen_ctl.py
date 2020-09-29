from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
 
# ドライバー
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.google.com/")
 
# 検索キーワード
search_box = driver.find_element_by_name("q")
search_box.send_keys("Glay")
time.sleep(0.5)

# 検索実行
search_btn = driver.find_element_by_name("btnK")
search_btn.click()