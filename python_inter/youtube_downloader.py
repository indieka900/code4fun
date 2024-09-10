from pytube import YouTube

link = input("Enter the YouTube Url for the video\n")
video = YouTube(url=link)
typ = input("Reply 1 for audio and 2 for video: ")
if typ == 1:
    stream = video.streams.get_audio_only()
else:
    stream = video.streams.get_highest_resolution()
print("****************hello***************")
stream.download()