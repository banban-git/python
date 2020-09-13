import youtube_dl

#動画URL
#download_url = 'https://www.youtube.com/watch?v=AVJAN6t6BDs&feature=youtu.be'
download_url = input("YouTube動画URLを入力して下さい：")
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','format':'best'})
with ydl: result = ydl.extract_info(download_url, download=True)
input("ダウンロード完了　(格納場所　C:\work\python\\" + result['title'] + ".mp4 )")