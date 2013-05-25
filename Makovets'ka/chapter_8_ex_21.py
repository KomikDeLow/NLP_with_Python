#Using tree positions, list the subjects of the first 100 sentences
#in the Penn treebank, to make the results easier to view
# limit the extracted subjects to subtrees

import nltk
from nltk.corpus import *
sent=treebank.parsed_sents()[:100] # list of 100 sentences
list_NP_SBJ=[]
for j in sent: #buildibg a loop trough sentences
    for trees in j:
        test=''
        test=trees.node
        if test.startswith('NP-SBJ') and not trees.height()>3: #checking trees
            list_NP_SBJ.append(trees) #adding trees into a list

print 'Found subjects(NP-SBJ)trees wich height is less than 3 (means 2): ',len(list_NP_SBJ)
print '10 First Subjects'
for trees in list_NP_SBJ[:10]:
    print trees # Printing out the subjects of the sentenses

