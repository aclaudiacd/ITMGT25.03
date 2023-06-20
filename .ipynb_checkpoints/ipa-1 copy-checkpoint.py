from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=J5Jz4u8_J4U')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()