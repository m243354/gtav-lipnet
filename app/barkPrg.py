""" Bark Program
BarkAI is a GPT style text to speech AI.
We take our output from the LipNet code and produce speech through BarkAI.
"""
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from IPython.display import display
from IPython.display import clear_output
from multiprocessing import Process
import threading
import time, random

def audio_process(word_string, voiceType):
  #Threading helper function that takes in a string word_string and a string of the voice model type
  audio_array = generate_audio(word_string, history_prompt=voiceType) #v2/enspeaker is the voice model
  display(Audio(audio_array, rate=SAMPLE_RATE, autoplay=True))

def main():
  #type of voice in barkAI
  voiceType = 
    ["v2/en_speaker_0",
    "v2/en_speaker_1",
    "v2/en_speaker_2",
    "v2/en_speaker_3",
    "v2/en_speaker_4",
    "v2/en_speaker_5",
    "v2/en_speaker_6",
    "v2/en_speaker_7",
    "v2/en_speaker_8",
    "v2/en_speaker_9"]

  textwords = ["","",""] #input array
  flag = 0
  while "q/c" not in textwords:
    if flag == 0:
      textwords[0] = input("Enter:")
    elif flag == 1:
      textwords[1] = input("Enter:")
    else:
      textwords[0] = input("Enter:")
      flag = 0

    if "q/c" in textwords:
      clear_output() #clears the terminal
    else:
      #thread buffer for word processing
      if flag == 0:
        threading.Thread(target=audio_process,args=(textwords[0],voiceType[0])).start()
        flag+=1
      elif flag == 1:
        threading.Thread(target=audio_process,args=(textwords[1],voiceType[0])).start()
        flag+=1
      else:
        #wait for threads to finish task
        time.sleep(1)

if __name__ == '__main__':
  main()


