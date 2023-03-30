# Using Streamlit to host on huggingface spaces


# imports
import streamlit as st
from annotator.utils import *
st.set_page_config(layout='wide')
from pathlib import Path



# set path
SRT_PATH = Path('caption')
AUDIO_PATH = Path('./audio')

if not SRT_PATH.exists(): SRT_PATH.mkdir(exist_ok=True)
if not AUDIO_PATH.exists(): AUDIO_PATH.mkdir(exist_ok=True)


def make_sidebar():
    with st.sidebar:
        st.markdown('### auto-YT-annotator')
        st.write('Link to the GitHub Repo')


@st.cache(allow_output_mutation=True)
def caption_from_url(url : str):
    audio_src = get_audio(url)
    annotation = annotate(audio_src)
    result = get_caption(annotation)

    return result

# === main === #
def main():
    url, name = None, None
    make_sidebar()

    # place holder video
    demo_url = 'https://youtu.be/ORMx45xqWkA'
    col1, col2 = st.columns([1.2, 1])

    with col1:
        url = st.text_input('Enter URL for the YouTube video', demo_url)
        st.video(url)

    with col2:
        default_opt = 'Generate Caption'
        opt = st.radio('What do you wish to do?', ['Generate subtitles for the entire video'])

        if st.button('Generate Caption'):
            result = caption_from_url(url)
            name = Path(audio_src).stem
            with working_directory(SRT_PATH):
                write_caption(result, name)

        if name is not None:
            with working_directory(SRT_PATH):
                with open(f'{name}.srt') as f:
                    st.download_button('Download Caption', f, file_name=f'{name}.srt')



if __name__ == '__main__':
    main()
