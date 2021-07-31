import youtube_dl

# 動画URL
# download_url = 'https://www.youtube.com/watch?v=CVNW-57FLzI'
download_url = input("YouTube動画URLを入力して下さい：")
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s', 'format': 'best'})
with ydl: result = ydl.extract_info(download_url, download=True)
