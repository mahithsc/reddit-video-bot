from moviepy.editor import concatenate_videoclips, VideoFileClip, CompositeVideoClip, AudioFileClip, ImageClip


def make_video_from_data():
    # title audio
    titleAudio = AudioFileClip('./video_assets/titleTTS.mp3')
    duration = titleAudio.duration

    # the title
    titleVideoClip = VideoFileClip("./initial_assets/minecraft.mp4").subclip(10,10+duration).without_audio()
    titleImageClip = ImageClip("./video_assets/title.png", duration=duration).set_position('center')
    titleComposite = CompositeVideoClip([titleVideoClip, titleImageClip])

    titleComposite.audio = titleAudio


    # comment audio
    commentAudio = AudioFileClip('./video_assets/commentTTS.mp3')
    commentDuration = commentAudio.duration
    # the comment
    commentVideoClip = VideoFileClip("./initial_assets/minecraft.mp4").subclip(10+duration,10+duration+commentDuration).without_audio()
    commentImageClip = ImageClip("./video_assets/comment.png", duration=commentDuration).set_position('center')
    commentComposite = CompositeVideoClip([commentVideoClip, commentImageClip])

    commentComposite.audio = commentAudio

    # conncatinating the two of the
    final = concatenate_videoclips([titleComposite, commentComposite])

    # creating the video
    final.write_videofile("./final/reddit-video.mp4")