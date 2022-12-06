from moviepy.editor import VideoClip, concatenate_videoclips, VideoFileClip, afx, TextClip, CompositeVideoClip, AudioFileClip, ImageClip

titleVideoClip = VideoFileClip("minecraft.mp4").subclip(10,15).without_audio()
titleImageClip = ImageClip("./video_assets/title.png", duration=5).set_position('center')
titleComposite = CompositeVideoClip([titleVideoClip, titleImageClip])

commentVideoClip = VideoFileClip("minecraft.mp4").subclip(15,20).without_audio()
commentImageClip = ImageClip("./video_assets/comment.png", duration=5).set_position('center')
commentComposite = CompositeVideoClip([commentVideoClip, commentImageClip])

final = concatenate_videoclips([titleComposite, commentComposite])



final.write_videofile("final.mp4")