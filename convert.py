import moviepy.editor as mp

# Load the MP4 video file
video = mp.VideoFileClip("myvideo.mp4")

# Extract the audio from the video
audio = video.audio

# Write the audio to an MP3 file
audio.write_audiofile("audio.mp3")
print('done')
