import streamlit as st
from pathlib import Path
from extract_text import YoutubeTextExtractor
from utils import is_from_youtube, get_youtube_id
from translator import TranslatorFactory
from config import DEFAULT_CONFIG

st.title("Video Translator")
st.text("Web tool kit for downloading, translating, transcribing, generating video")

# Sidebar for language selection only
st.sidebar.title('Settings ⚙️')
source_lang = st.sidebar.selectbox('Source Language:', ['en', 'it'], 
                                 index=0 if DEFAULT_CONFIG['language']['source'] == 'en' else 1)
target_lang = st.sidebar.selectbox('Target Language:', ['it', 'en'], 
                                 index=0 if DEFAULT_CONFIG['language']['target'] == 'it' else 1)

# Main input area
st.subheader("Video Input")
video_input = st.text_input("Enter video URL or upload a file below", 
                           value="https://www.youtube.com/watch?v=KG0Q05Lnm7s")

uploaded_file = st.file_uploader("Or upload a video file", type=['mp4', 'avi'])

# Show video preview
if video_input and is_from_youtube(video_input):
    st.video(video_input)
elif uploaded_file:
    st.video(uploaded_file)

# Translation settings
st.subheader("Translation Settings")
output_format = st.selectbox("Output format:", ["Text", "JSON"], 
                           index=0 if DEFAULT_CONFIG['output']['format'] == 'txt' else 1)

# Process button
if st.button('Translate Video'):
    with st.spinner('Processing video...'):
        try:
            # Initialize translator
            translator = TranslatorFactory.create_translator(DEFAULT_CONFIG)
            
            if video_input and is_from_youtube(video_input):
                video_id = get_youtube_id(video_input)
                text_extractor = YoutubeTextExtractor(output_format.lower())
                
                # Get transcript
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Transcript")
                    transcript = text_extractor.get_transcript_from_id(video_id)
                    st.text_area('', transcript, height=300)
                
                # Translate
                with col2:
                    st.subheader("Translation")
                    translation = translator.translate_text(
                        transcript, 
                        target_language=target_lang,
                        source_language=source_lang
                    )
                    st.text_area('', translation, height=300)
                
            elif uploaded_file:
                # Handle uploaded file using OpenAI's transcribe and translate
                temp_path = Path("temp_video.mp4")
                temp_path.write_bytes(uploaded_file.read())
                
                result = translator.translate_video(
                    str(temp_path),
                    target_language=target_lang
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Transcript")
                    st.text_area('', result['original_text'], height=300)
                
                with col2:
                    st.subheader("Translation")
                    st.text_area('', result['translated_text'], height=300)
                
                temp_path.unlink()  # Clean up temp file
                
            st.success('Translation completed!')
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")