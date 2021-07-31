import sys
import MeCab
m = MeCab.Tagger ("-Ochasen")
print(m.parse ("私の名前は平尾です。"))