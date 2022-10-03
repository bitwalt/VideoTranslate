import streamlit as st
from config import cfg, TRANSLATOR_MODELS, SP2_MODELS
from extract_text import YoutubeTextExtractor
from utils import is_from_youtube, get_youtube_id


#  ==== SIDEBAR ====
        
st.sidebar.title('Navigation Menu ⬇️')
st.sidebar.subheader("Input")
input_video_type = st.sidebar.radio('Select input video:', ["Url", "File"])
st.sidebar.subheader("Translator")
source, dest = st.sidebar.radio('Path:', ['en-it', 'it-en']).split("-")
# trans_model = st.sidebar.radio('Select Model:', TRANSLATOR_MODELS)
# st.sidebar.subheader("Speech2Text AI model")
# s2t_model = st.sidebar.radio('Select Model', SP2_MODELS)

st.title("Video Translator")
st.text("""Web tool kit for downloading, translating, transcribing, generating video""" )

#  ==== INPUT ====

input_container = st.container()
if input_video_type == "Url":
    video_input = input_container.text_input("Insert video url here", value="https://www.youtube.com/watch?v=KG0Q05Lnm7s")
    if video_input and is_from_youtube(video_input):
        if input_container.button("Show"):
            input_container.video(video_input)      
else: 
    video_input = st.file_uploader("Upload Video",type=['mp4', 'avi'])

st.subheader("Transcript and Translate")
st.write("Extract and translate captions using youtube_transcript_api")
formatter = st.selectbox("Select formatter: ", ["Text", "JSON"])

col1, col2 = st.columns(2)

if input_video_type == "Url" and is_from_youtube(video_input):
    video_id = get_youtube_id(video_input)
    if st.button('Run'):     
        with st.spinner('Extracting captions from given video'):
            text_extractor = YoutubeTextExtractor(formatter)
            transcript = text_extractor.get_transcript_from_id(video_id)    
            if formatter == "JSON":
                col1.json(transcript)
            else:
                col1.text_area('Text Transcription', transcript)          
        with st.spinner('Translating captions from given video'):
            translated_transcript = YoutubeTextExtractor.translate_from_id(video_id, source, dest)    
            col2.json(translated_transcript)
                    

#         with st.spinner('Translating Text...'):
#             result = translator.translate(text, src=f'{source}', dest=f'{dst}').text
#         st.subheader("Translated Text is ...")
#         st.write(result) 

#         st.write('')
#         st.header('Generated Audio')
        
#         with st.spinner('Generating Audio ...'):
#             ta_tts2 = gTTS(result,lang=f'{dst}')
#             ta_tts2.save('trans2.mp3')
#         st.audio('trans2.mp3',format='audio/mp3')  
#         st.balloons()  
               
            
#     else:
#         st.subheader('Image not found! Please Upload an Image.')