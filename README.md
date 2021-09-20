# 環境構築

１）Gitをインストール
https://gitforwindows.org/
<img src="install/gitInstall.png">

２）GitHubに接続（下記を参照）
https://qiita.com/hollyhock0518/items/a3fee20951cd92c87ed9
<img src="install/gitHub.png">

３）python3.6.8をインストール
インストールフォルダの下記のファイルを実行
> install/python-3.6.8-amd64.exe

**インストール時は、パスを追加にチェックをいれる**
<img src="install/python_installer.png">

４）VsCodeをインストール  
https://eng-entrance.com/texteditor-vscode
<img src="install/VisualStudioCode.png">  

５）レポジトリをダウンロード  
作業フォルダを作成して、下記のコマンドを実行
```
git clone https://github.com/banban-git/python.git
```

６）Visual Studioでpythonレポジトリを取り込む  
フォルダを開く　→ 5) でクローンしたレポジトリを選択
<img src="install/VisualStudioCode_project.png">


# ライブラリインストール
コマンドを実行し、ライブラリをインストールする。

```
pip install -r requirements.txt
```

# OCRをインストール
https://gammasoft.jp/blog/tesseract-ocr-install-on-windows/

# ■機械学習
作業フォルダ
> src/machine_learning
  

## ・画像取得
JPEGファイルを  
指定文字列『検索文字』で100件取得します。
```python
python bing_scraper.py --search '炭治郎' --format 'jpg' --limit 20 --download --chromedriver chromedriver/chromedriver.exe
```

## ・画像解析
学習回数＝1000回にしています。精度を上げたい場合は、  
--how_many_training_steps=**1000**　←ここの数字を変更してください
```python
python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps=100 --model_dir=inception --summaries_dir=training_summaries/basic --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --image_dir=images
```
## ・実行
判別したい画像⇒ 『hanbetu1.jpg』
```
python label_image.py --graph=retrained_graph.pb --labels=retrained_labels.txt --output_layer=final_result --image=images_test/hanbetu6.jpg --input_layer=Placeholder
```


pyxeleditor raa
pyxeleditor raa

# setting.json(作業メモ)
変更前
```
"python.pythonPath": "\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe",
```
変更後
```
"python.pythonPath": "C:\\Program Files\Python36\\python.exe",
```
