from converter import Converter
"""
Program that will take a video filename input and convert this video from an .mp4 into an .mpg so that the main GTAV program can run predictions on it.
"""

def main():
	#converter object
	conv = Converter()
	fName = input("Input video filename to convert:\n")
	info = conv.probe("\\wsl$\\Ubuntu-22.04\\home\\m243354\\gtav-lipnet\\data\\videoConvTest")

	#PATH = '\\wsl$/Ubuntu-22.04/home/m243354/gtav-lipnet/data/videoConvTest'

	convert = conv.convert(fName + '.mp4', fName + '.mpg', {
	    'format': 'mp4',
	    'audio': {
	        'codec': 'aac',
	        'samplerate': 11025,
	        'channels': 2
	    },
	    'video': {
	        'codec': 'hevc',
	        'width': 320,
	        'height': 288,
	        'fps': 25
	    }}
	)



if __name__ == '__main__':
	main()