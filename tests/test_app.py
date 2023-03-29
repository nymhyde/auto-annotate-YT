from utils import *
import os

working_dir = os.getcwd()

def test_check():
    url = 'https://youtu.be/ORMx45xqWkA'
    audio_src = get_audio(url)
    annotation = annotate(audio_src)
    caption = get_caption(annotation)
    write_caption(caption, 'first')

    assert os.path.isfile(working_dir+'/caption/first.srt') == True
