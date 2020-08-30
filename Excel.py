import openpyxl

# 新規作成
book = openpyxl.Workbook()

# シート設定
sheet = book.worksheets[0]
# シートのタイトル変更
sheet.title = 'サンプル'
# シート追加
new_sheet = book.create_sheet('追加シート')

# 保存
book.save('testFile.xlsx')
# 終了
book.close()