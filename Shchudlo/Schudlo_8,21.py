# fine

#Building a simple program which extracts subjects from first 100 sentenses
#in the Penn bank tree
import nltk
from nltk.corpus import *

sentenses=treebank.parsed_sents()[:100] # Building list of 100 first sentenses

list_of_NP_SBJ=[]
for i in sentenses:# building a loop through sentenses and their trees
	for tree in i:
		test=''
		test=tree.node
		if test.startswith('NP-SBJ') and not tree.height()>3: # Cheking trees to be Subjects and of height not bigger than 3
			list_of_NP_SBJ.append(tree) # Adding needed trees into a list

print 'Found subjects(NP-SBJ)trees wich height is less than 3 (means 2): ',len(list_of_NP_SBJ)
print '10 First Subjects'
for tree in list_of_NP_SBJ[:10]:
    print tree # Printing out the subjects of the sentenses
