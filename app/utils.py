import tensorflow as tf
from typing import List
import cv2
import os 

#File of helper functions for the streamlit application

vocab = [x for x in "abcdefghijklmnopqrstuvwxyz'?!123456789 "]
char_to_num = tf.keras.layers.StringLookup(vocabulary=vocab, oov_token="")
# Mapping integers back to original characters
num_to_char = tf.keras.layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True
)


def load_video(path:str) -> List[float]: 
    #Take an input video and return a list of tensor data from the video
    cap = cv2.VideoCapture(path)
    frames = []
    missing_frames = []
    for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))): 
        ret, frame = cap.read()
        if frame is None:
            #stackOF solution to skip reading frames that openCV cannot read from
            missing_frames.append(frame)
            continue

        frame = tf.image.rgb_to_grayscale(frame)
        frames.append(frame[190:236,80:220,:])

    cap.release()
    mean = tf.math.reduce_mean(frames)
    std = tf.math.reduce_std(tf.cast(frames, tf.float32))
    return tf.cast((frames - mean), tf.float32) / std
    
def load_alignments(path:str) -> List[str]: 
    #Take an input video path and return a list of alignment data
    with open(path, 'r') as f: 
        lines = f.readlines() 
    tokens = []
    for line in lines:
        line = line.split()
        if line[2] != 'sil': 
            tokens = [*tokens,' ',line[2]]
    return char_to_num(tf.reshape(tf.strings.unicode_split(tokens, input_encoding='UTF-8'), (-1)))[1:]

def load_data(path:str): 
    #Takes in a video path to the alingments folder and returns the video frames and alignments for the neural network
    path = bytes.decode(path.numpy())
    file_name = path.split('/')[-1].split('.')[0]
    # File name splitting for windows
    #file_name = path.split('\\')[-1].split('.')[0]
    video_path = os.path.join('..','data','s1',f'{file_name}.mpg')
    alignment_path = os.path.join('..','data','alignments','s1',f'{file_name}.align')
    frames = load_video(video_path) 
    alignments = load_alignments(alignment_path)
    
    return frames, alignments

def load_data_noAlign(path:str): 
    #Takes in a video path and loads it for no alingments
    path = bytes.decode(path.numpy())
    file_name = path.split('/')[-1].split('.')[0]
    # File name splitting for windows
    #file_name = path.split('\\')[-1].split('.')[0]
    #video path is partially hard coded for the 
    video_path = os.path.join('..','data','myVideos',f'{file_name}.mpg')
    frames = load_video(video_path) 
    
    return frames