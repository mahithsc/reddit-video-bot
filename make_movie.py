from moviepy.editor import concatenate_videoclips, VideoFileClip, CompositeVideoClip, AudioFileClip, ImageClip

# the title
titleVideoClip = VideoFileClip("minecraft.mp4").subclip(10,15).without_audio()
titleImageClip = ImageClip("./video_assets/title.png", duration=5).set_position('center')
titleComposite = CompositeVideoClip([titleVideoClip, titleImageClip])

titleAudio = AudioFileClip('./video_assets/titleTTS.mp3')
titleComposite.audio = titleAudio

# the comment
commentVideoClip = VideoFileClip("minecraft.mp4").subclip(15,20).without_audio()
commentImageClip = ImageClip("./video_assets/comment.png", duration=5).set_position('center')
commentComposite = CompositeVideoClip([commentVideoClip, commentImageClip])

# conncatinating the two of the
final = concatenate_videoclips([titleComposite, commentComposite])

# creating the video
final.write_videofile("final.mp4")