# All your files aren't Python modules
# Add  docstring to the function

# Petrukha Tetiana Als-11
# Chapter_5, Ex_8

# Create a dictionary e, to represent a single lexical entry for some word of your choice.
# Define keys such as headword, part-of-speech, sense, and example, and assign them suitable values.

import nltk
e = nltk.defaultdict(list) # function to create default value
def dic(headword,part_of_speech,sense,example):
	e[headword]=[part_of_speech,sense,example]
	
dic('squirrel','N','is a small animal with a long furry tail','The future of the red squirrel in scotland is also far from secure.')
dic('bird','N','is a creature with feathers and wings','Loud Bird song is far more pleasant than equally loud beeping.') # Create a dictionary
print e ['bird']  # print a dictionary


