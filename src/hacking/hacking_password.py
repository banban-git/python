import time 
import getpass
from itertools import product
import seqgentools as seq

# パスワード
target = "test"
print("あなたが入力したパスワードを解析中.....")
# 入力可能文字
chars = '0123456789abcdefghijklmnopqrstuvwxyz'

# チェック関数
def check(chars, repeat):
    # 全パターン取得（https://docs.python.org/ja/3/library/itertools.html)
    pws = product(chars, repeat=repeat)
    for pwObj in pws:
        password = ''.join(pwObj)
        if (password == target): 
            return password
# 実行
start = time.time()
pw = check(chars, len(target))

if (pw is None): 
    print('失敗')
else: 
    print('パスワードが見つかりました -->', pw)

finish = time.time() - start
print(round(finish, 2) , "秒")