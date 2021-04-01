#it's work
from moviepy.editor import *
clip = VideoFileClip('aa.mp4')
clip.write_gif('my_gif.gif')