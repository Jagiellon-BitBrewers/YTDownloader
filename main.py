from pytube import YouTube

PATH = 'C:\Youtube Downloader\downloaded'

# printing welcome phrase
print("""
Welcome in
_____.___.___________________                      .__                    .___            
\__  |   |\__    ___/\______ \   ______  _  ______ |  |   _________     __| _/___________ 
 /   |   |  |    |    |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ |
 \____   |  |    |    |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
 / ______|  |____|   /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
 \/                          \/                  \/                \/      \/    \/       

""")

video_url = input('Enter the url of the video you want to download: \n')


try:
    yt = YouTube(video_url)
    print('Downloading...')
    yt.streams.first().download(output_path=PATH)
    print(f'Your video has been downloaded to a folder: {PATH}')
except:
    print("Something isn't right")