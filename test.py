from pytube import YouTube, Playlist, Channel, Search

#* creating YouTube object called yt
yt = YouTube('https://youtu.be/KQetemT1sWc?si=6092GurV9ouLiJj_')

#* creating a playlist object by initializing the object with a playlist URL or from a video link in a plalist
p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

#* creating a channel object
# c = Channel('https://www.youtube.com/@NIGHTRIDEPL')

#* creating search object
s = Search('Nightride')
# print(s.completion_suggestions)

#* by using code en.nP7-2PuUl7o we're accessing english subtitles
# caption = yt.captions.get_by_language_code('en.nP7-2PuUl7o')
#*printing formated subtitles
# caption.generate_srt_captions()

#* searching for streams that don't have audio using .filter()
# for i in yt.streams.filter(only_video=True):
#     print(i)

#* getting stream by it's itag
# stream = yt.streams.get_by_itag(137)
# stream.download()
