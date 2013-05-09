import nltk
def subsumes(fas1,fas2):      # writing a function which holds two features which may be unified
	for w in fas1:
		if w in fas2  and fas2>fas1:
			print fas1.unify(fas2)
		else:
			print 'This structures dont subsemes'
fas1 = nltk.FeatStruct(NUMBER=25)
fas2 = nltk.FeatStruct(NUMBER=25, STREET='rue Pascal')
print subsumes(fas1,fas2)
fs1 = nltk.FeatStruct(NUMBER=25)
fs2 = nltk.FeatStruct(NUMBER=53,STREET = 'rue Pascal')
print subsumes(fs1,fs2)
# as we see by the result this structures do not subsumess
