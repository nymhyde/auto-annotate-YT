# Using Streamlit to host on huggingface spaces


# imports
import streamlit as st
from annotator.utils import *
st.set_page_config(layout='wide')
from fastcore.xtras import globtastic
from pathlib import Path
import subprocess



# set path
SRT_PATH = Path('caption')
AUDIO_PATH = Path('audio')

if not SRT_PATH.exists(): SRT_PATH.mkdir(exist_ok=True)
if not AUDIO_PATH.exists(): AUDIO_PATH.mkdir(exist_ok=True)



