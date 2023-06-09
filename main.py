import streamlit as st

st.text("hello Streamlit!")

import pytesseract
from PIL import Image
import cv2
import matplotlib.pyplot as plt


path = './nobrand.jpg'

img = Image.open(path)
st.image(img, width = 200)

image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
st.text(text)


import ffmpeg
import whisper
from asrecognition import ASREngine
st.header("Trascribe your Audio")
filepath = st.text_input(label='please enter the path to the file')

import speech_recognition as sr
#import sys #-- 텍스트 저장시 사용

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    speech = r.listen(source)

#sys.stdout = open('audio_output.txt', 'w') #-- 텍스트 저장시 사용

try:
    audio = r.recognize_google(speech, language="ko-KR")
    print("Your speech thinks like\n " + audio)
except sr.UnknownValueError:
    print("Your speech can not understand")
except sr.RequestError as e:
    print("Request Error!; {0}".format(e))
    
# model = whisper.load_model("base")
# from IPython.display import Audio
# Audio("./aaa.mp3")
# def transcribe(audio):
    
#     # load audio and pad/trim it to fit 30 seconds
#     audio = whisper.load_audio(audio)
#     audio = whisper.pad_or_trim(audio)

#     # make log-Mel spectrogram and move to the same device as the model
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)

#     # detect the spoken language
#     _, probs = model.detect_language(mel)
#     print(f"Detected language: {max(probs, key=probs.get)}")

#     # decode the audio
#     options = whisper.DecodingOptions(fp16=False)
#     result = whisper.decode(model, mel, options)
#     return result.text

# easy_text = transcribe("./aaa.mp3")
# st.text(easy_text)

import bardapi
import os
os.environ['_BARD_API_KEY']='WwhjGcfngiK0STZR7o3fdNL3Kn25k1elab5Y-AuJKhDYpS64msPT_Tfsv6OyKppZsZv_mQ.'



input_text = '나는 메밀 알레르기가 있어 이 음식을 먹어도 될까?' + text 
li = []
response = bardapi.core.Bard().get_answer(input_text)
for i , choice in enumerate(response['choices']):
##    li.append(f"Choice {i+1}:\n", choice['content'][0], "\n")
    li.append(choice['content'][0])
    
st.markdown(li[0])

input_text = easy_text
li = []
response = bardapi.core.Bard().get_answer(input_text)
for i , choice in enumerate(response['choices']):
##    li.append(f"Choice {i+1}:\n", choice['content'][0], "\n")
    li.append(choice['content'][0])
    
st.markdown(li[0])
