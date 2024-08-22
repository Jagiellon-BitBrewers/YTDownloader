import yt_dlp

#!! change to your path if you want
PATH = 'Downloaded/'

# printing welcome phrase
print(r"""
Welcome in
_____.___.___________________                      .__                    .___            
\__  |   |\__    ___/\______ \   ______  _  ______ |  |   _________     __| _/___________ 
 /   |   |  |    |    |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ |
 \____   |  |    |    |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
 / ______|  |____|   /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
 \/                          \/                  \/                \/      \/    \/       

""")

video_url = input('Enter the url of the video you want to download: \n')

def my_hook(d):
    if d['status'] == 'finished':
        print('\nDone downloading, now post-processing ...')

ydl_opts = {
    'format': 'best',
    'outtmpl': f'{PATH}%(title)s.%(ext)s',
    #'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_url)