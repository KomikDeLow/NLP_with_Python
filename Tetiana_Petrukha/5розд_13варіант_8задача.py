# All your files aren't Python modules
#
import nltk
e = nltk.defaultdict(list)
def dic(headword,part_of_speech,sense,example):
	e[headword]=[part_of_speech,sense,example]
dic('squirrel','N','is a small animal with a long furry tail','The future of the red squirrel in scotland is also far from secure.')
dic('bird','N','is a creature with feathers and wings','Loud Bird song is far more pleasant than equally loud beeping.')
print e ['bird']


