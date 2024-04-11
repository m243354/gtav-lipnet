# Give Them A Voice

Welcome to the repository for Give Them A Voice

## Getting started
Dependencies
- Your device must have a camera.
- Minimum system requirements: Ubuntu 20.04, python3, able to install all packages
- Before starting, run `sudo apt-get upgrade` to be sure your Ubuntu installation is up to date.
- Next, run `pip install -r dependencies.txt`
- After pip installing all of the requried python libraries, you must install the barkAI package, ffpmeg, and PythonVideoConverter. 
### Installing BarkAI
Navigate to any desired directory and then run these lines:
```
git clone https://github.com/suno-ai/bark 
cd bark && pip install . 
```
OR RUN THESE LINES:
`pip install git+https://github.com/suno-ai/bark.git`

### Installing PythonVideoConverter
In order to run the project on your own data, you will record a video in mp4 or in mpg. In order to assist those whose devices only recode in mp4, we included a converter script. To use this converter script you must install ffpmeg and PythonVideoConverter. Download the package from PyPi at: https://pypi.org/project/PythonVideoConverter/ to any desired directory.
Navigate to the downloaded location and then run these lines:
```
python3 setup.py install
pip install ffpmeg
```
To run the script on a video you wish to convert, type python3 vidConv.py. The program will produce guided output to convert the video. 

## Running the project
```streamlit run gtav.py```
After running this in ubuntu, you will have an IP address supplied to you. Go to this address and you will be able to interact with the project. At its base level, the project will work with a pre-trained voice model. To get the project to work with your own video input, record a video of max 10 seconds in length and place it in the `gtav-lipnet/data/myVideos` folder. From there, refresh the app and select the filename in the dropdown and see the model produce a lipreading approximation of your video! 
# Todo(remove before cappy day)
- TODO: Make video conversion from mp4 to mpg
- TODO: Crop video into the required size for the program
- TODO: Fix barkAI installation on my laptop so I get sound output

### Unnecessary but nice todo
- TODO: Make a script to grab the IP and send the browser to it automatically.
- TODO: Windows functionality stuff. All code is in Ubuntu rn.
- TODO: Make website look nicer
- TODO: Ensure smooth file conventions so the user can navigate nicely. Put READMEs in each file folder to explain its purpose
- TODO: Write comments in ALL code for ALL functions and ALL features
- TODO: Live Video Capture and conver
