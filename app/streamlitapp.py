# Import all of the dependencies
import streamlit as st
import os 
import imageio 
import tensorflow as tf 
from utils import load_data, num_to_char, load_data_noAlign
from modelutil import load_model

#broken import -_-
#from barkPrg import audio_process

#Make the streamlit app read an input video from the user
#take input video and run model on it
#after model is complete, send output to barkAi prg
#bark program optimizations for low RAM 
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
model = load_model()


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
st.link_button("GTAV Github Repository", "https://github.com/m243354/gtav-lipnet")
# Generate two columns 
vidFile = 'video1.mp4'
vidFile = 'bbal8p.mpg'
#todo find directory name and fix this nonsense
#dirname = os.path.dirname()
col1, col2 = st.columns(2)
with col1:     
    #st.info('INPUT VIDEO BELOW')

    #file_path = os.path.join('..','data','s1', selected_video) TODO make live camera frames
    #os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')
    #generate a list of all the files within myVideos
    videoList = os.listdir(os.path.join('..', 'data', 'myVideos'))
    videoList = os.listdir(os.path.join('..', 'data','s3','s3')) #s3 mod
    selected_video = st.selectbox('Choose video from myVideos directory:', videoList)    
    #vidPath = videoList+selected_video
    
    #st.text(selected_video)

    # Video display
    displayVP = os.path.join('..','data','myVideos',selected_video)
    displayVP = os.path.join('..', 'data','s3','s3', selected_video)
    #video = open(displayVP, 'rb') 
    #video_bytes = video.read() 
    #st.text(displayVP)
    #st.video(selected_video)
    st.image("blayne.PNG")

with col2:
    #st.button("START", on_click=startVid())
    #st.button("STOP", on_click=stopVid())
    #st.button("PLAY", on_click=playButton()) 


    voice = st.selectbox("Choose AI Voice model:", voiceType)
    st.text("Decoded text will be outputted here:")

    #
    video = load_data_noAlign(tf.convert_to_tensor(selected_video))
    yhat = model.predict(tf.expand_dims(video, axis=0))
    decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
    # Convert prediction to text
    converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
    #converted_prediction = "Text output for video here."
    st.text(converted_prediction)

    #converted prediction is text to be sent to the barkAI application. Uncomment this line below to hear the results of the prediction in voice mode
    #audio_process(converted_prediction, voice)
    
st.image("goat.png", caption="Throat Goats", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
