import streamlit as st
from PIL import Image
import numpy as np
from config import cfg, TRANSLATOR_MODELS, SP2_MODELS


def language_selector():
    src = st.sidebar.selectbox("From Language",['English','Italian'])
    destination = st.sidebar.selectbox("To Language",['Italian','English'])
    helper = {'Italian':'it','English':'en'}
    dest = helper[destination]
    source = helper[src]
    return source, dest


st.title("Bitcoin Video Translator")

st.write("Web tool kit for downloading, translating, transcribing, generating video. "
         "Created to disseminate educational resources on bitcoin." )
st.sidebar.title('Navigation Menu ⬇️')
st.sidebar.subheader("Input")
input_video = st.sidebar.radio('Select input video:', ["Url", "File"])

st.sidebar.subheader("Translator")
trans_model = st.sidebar.radio('Select Model:', TRANSLATOR_MODELS)
source, dest = st.sidebar.radio('Path:', ['en-it', 'it-en']).split("-")

st.sidebar.subheader("Speech2Text AI model")
s2t_model = st.sidebar.radio('Select Model', SP2_MODELS)
st.sidebar.subheader("Ouput")


#  ==== INPUT ====

if input_video == "Url":
    # st.write("Example: https://www.youtube.com/watch?v=KG0Q05Lnm7s")
    video_url = st.text_input("Insert video url here", )
else: 
    video_file = st.file_uploader("Upload Video",type=['mp4', 'avi'])

#  ==== OUTPUT ====

options = st.multiselect(
        'Select Options for this video', 
        ['Show', 'Download', 'Transcript', 'Translate'])

if st.button("Run"):
    st.video(video_url)
    
    if st.button("Download"):
        # TODO: Download video
        st.video(video_url)


def extract_captions(video):
    raise NotImplementedError


def translate(text):
    pass

#  if st.sidebar.button("Translate!"):
#     if len(area)!=0:
#         sour = translator.detect(area).lang
        
#         answer = translator.translate(area, src=f'{sour}', dest=f'{dst}').text
#         #st.sidebar.text('Answer')
#         st.sidebar.text_area("Answer",answer)
#         st.balloons()
#     else:
#         st.sidebar.subheader('Enter Text!')    


# st.set_option('deprecation.showfileUploaderEncoding',False)
# st.title('AI OCR')
# st.subheader('Optical Character Recognition with Voice output')
# st.text('Select source Language from the Sidebar.')

# image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])


# text = "With property rights, free speech and a functioning legal system."
# st.write(text)
# if st.button("Translate"):
#     result = translator.translate(text, dest='it')
#     # result = translator.translate(text, src=f'{source}', dest=f'{dst}').text
#     st.write(result)
    
    
# if st.button("Convert"):
    
#     if image_file is not None:
#         img = Image.open(image_file)
#         img = np.array(img)
        
#         st.subheader('Image you Uploaded...')
#         st.image(image_file,width=450)
        
#         if src=='English':
#             with st.spinner('Extracting Text from given Image'):
#                 eng_reader = easyocr.Reader(['en'])
#                 detected_text = eng_reader.readtext(img)
#             st.subheader('Extracted text is ...')
#             text = display_text(detected_text)
#             st.write(text)
            

#         elif src=='Italian':
#             with st.spinner('Extracting Text from given Image'):
#                 swahili_reader = easyocr.Reader(['it'])
#                 detected_text = swahili_reader.readtext(img)
#             st.subheader('Extracted text is ...')
#             text = display_text(detected_text)
#             st.write(text)
              
#         st.write('')
#         ta_tts = gTTS(text,lang=f'{source}')
#         ta_tts.save('trans.mp3')
#         st.audio('trans.mp3',format='audio/mp3')
        

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