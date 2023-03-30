# imports
import re, os, subprocess
from pathlib import Path
import torch
import whisper
from pytube import YouTube
import pandas as pd
from fastcore.foundation import working_directory


# os.chdir('../')

def start_app():
    subprocess.run(['streamlit', 'run', 'app.py'])



# Download the YT video as audio format
def get_audio(url : str):
    audio_path = Path('./audio')
    with working_directory(audio_path):
        audio_input = YouTube(url).streams.filter(only_audio=True).last()
        audio_input = audio_input.download()

    return audio_input


# transcribe function :: using 'base' model
def annotate(audio_src, model_size='base'):
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    model = whisper.load_model(model_size, device=device)
    annotation = model.transcribe(audio_src)

    return annotation

# convert transcribed result into pandaFrame and get the text
def get_caption(model_output : dict):
    return model_output['text']

# write caption file into .srt format
def write_caption(text : str, name : str):
    #srt_path = Path('./caption')
    # with working_directory(srt_path):
    with open(f"{name}.srt", "w") as f:
        f.write(text)
        f.close()



def get_segments(model_output : dict):
    df_segments = pd.DataFrame(model_output['segments'], columns=['id', 'start', 'end', 'text'])


# =========== test  ============== #
url = 'https://youtu.be/ORMx45xqWkA'
audio_src = get_audio(url)
annotation = annotate(audio_src)
caption = get_caption(annotation)
write_caption(caption, 'first')
