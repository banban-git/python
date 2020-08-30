import time 
import getpass
from itertools import product

# パスワード
target = "zzzzz"
print("あなたが入力したパスワードを解析中.....")
# 入力可能文字
chars = '0123456789abcdefghijklmnopqrstuvwxyz'
# 入力可能文字数
inputLength = len(target)

# チェック関数
def check(chars, repeat):
    pws = product(chars, repeat=repeat)
    for pwObj in pws:
        password = ''.join(pwObj)
        if (password == target): 
            return password
# 実行
start = time.time()
pw = check(chars, inputLength)

if (pw is None): 
    print('失敗')
else: 
    print('パスワードが見つかりました -->', pw)

finish = time.time() - start
print(round(finish, 2) , "秒");