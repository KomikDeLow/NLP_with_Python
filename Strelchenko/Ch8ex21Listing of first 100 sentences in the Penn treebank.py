import nltk
from nltk.corpus import *
sent=treebank.parsed_sents()[:100] # Building list of 100 first sentences
list_NP_SBJ=[]
for j in sent:# writing a condition for choosing sentences
  for trees in j:
    test=''
    test=trees.node
    if test.startswith('NP-SBJ') and not trees.height()>3: # Cheking if trees are subjects and have height not bigger than 3
      list_NP_SBJ.append(trees) # Adding  trees to a list

print 'Found subjects(NP-SBJ)trees wich height is less than 3 (means 2): ',len(list_NP_SBJ)
print '10 First Subjects'
for trees in list_NP_SBJ[:10]:
    print trees # output of the sentences
