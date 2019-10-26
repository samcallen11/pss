# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = 'Welcome to Iran here is my home my name is blackboard!'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
#slow ash ro motevageh nashodem
myobj = gTTS(text=mytext, lang=language, slow=True) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

# Playing the converted file 
os.system("mpg321 welcome.mp3") 
