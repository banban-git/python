from sys import argv
import MeCab
import markovify

# ファイル名
file_name = "C:/work/python/src/autoComposition/1_tax.text"    

def main():
    # ファイルオープン
    with open(file_name, "r",encoding="utf-8_sig") as file:
        text=file.read()
    # わかち書き
    tagger = MeCab.Tagger("-Owakati")
    text = tagger.parse(text)
    # マルコフ連鎖
    model = markovify.NewlineText(text, state_size=2)
    sentence = model.make_short_sentence(280)
    sentence = sentence.replace(" ", "")
    # 出力
    print(sentence)

if __name__== "__main__":
    main()