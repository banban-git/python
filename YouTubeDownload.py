import youtube_dl

#動画URL
download_url = 'https://www.youtube.com/watch?v=AVJAN6t6BDs&feature=youtu.be'
#ダウンロード
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s','format':'best'})
with ydl: result = ydl.extract_info(download_url, download=True)