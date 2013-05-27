# fine

#Extracts subjects from first 100 sentenses
#in the Penn bank tree

import nltk
from nltk.corpus import *

sent=treebank.parsed_sents()[:100] # Building list of 100 first sentenses

list_NP_SBJ=[]
for j in sent:# building a loop through sentenses and their trees
	for trees in j:
		test=''
		test=trees.node
		if test.startswith('NP-SBJ') and not trees.height()>3: # Cheking trees to be Subjects and of height not bigger than 3
			list_NP_SBJ.append(trees) # Adding needed trees into a list

print 'Found subjects(NP-SBJ)trees wich height is less than 3 (means 2): ',len(list_NP_SBJ)
print '10 First Subjects'
for trees in list_NP_SBJ[:10]:
    print trees # Printing out the subjects of the sentenses
