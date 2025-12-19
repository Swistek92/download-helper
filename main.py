import yt_dlp

# Link do playlisty YouTube
playlist_url = 'https://www.youtube.com/playlist?list=PLnxAksfQVKrakq3VtjZRlXP7x31BvFVJY'

# Ustawienia pobierania
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': False,
    'ignoreerrors': True,
    'quiet': False,
    'no_warnings': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
