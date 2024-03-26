# Import all of the dependencies
import streamlit as st
import os 
import imageio 

import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model

#Make the streamlit app read an input video from the user
#take input video and run model on it
#after model is complete, send output to barkAi prg

def startVid():
    #toggle camera on
    pass

def stopVid():
    #toggle camera off
    pass

def playButton():
    #idk Schaus said put it in here
    pass

#voiceModels
voiceType = ("v2/en_speaker_0",
  "v2/en_speaker_1",
  "v2/en_speaker_2",
  "v2/en_speaker_3",
  "v2/en_speaker_4",
  "v2/en_speaker_5",
  "v2/en_speaker_6",
  "v2/en_speaker_7",
  "v2/en_speaker_8",
  "v2/en_speaker_9")

# Set the layout to the streamlit app as wide 
st.set_page_config(layout='wide')

st.title('Give Them A Voice') 
st.link_button("GTAV Repository", "https://gitlab.usna.edu/m243354/gtav-lipnet")
# Generate two columns 
vidFile = 'video1.mp4'
col1, col2 = st.columns(2)
with col1:     
    st.info('INPUT VIDEO BELOW')
    #file_path = os.path.join('..','data','s1', selected_video) TODO make live camera frames
    #os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

    # Video display
    video = open(vidFile, 'rb') 
    video_bytes = video.read() 
    st.video(video_bytes)
    st.image("goat.png", caption="Throat Goats", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

with col2:
    st.button("START", on_click=startVid())
    st.button("STOP", on_click=stopVid())
    st.button("PLAY", on_click=playButton()) 
    #st.info('This is all the machine learning model sees when making a prediction')
    
    voice = st.selectbox("Choose AI Voice model:", voiceType)
    st.text("Decoded text will be outputted here:")
    #TODO fix AI model. Needs alignments from a test video to be generatead then saved into a corresponding folder.
    #video, annotations = load_data(tf.convert_to_tensor(vidFile))     
    #model = load_model()
    #yhat = model.predict(tf.expand_dims(video, axis=0))
    #decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
    #st.text(decoder)

    # Convert prediction to text
    #converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
    #st.text(converted_prediction)
    #converted prediction is text to be sent to the barkAI applicatio
    st.image("usna.png")
