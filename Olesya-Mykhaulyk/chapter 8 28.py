#Olesya Mykhaulyk
#ALs-12
#chapter 8 ex28
import nltk
from nltk.corpus import treebank
l = treebank.parsed_sents()[:10]# list of 10 syntactically analyzes trees
allproductions = []# list for the rules
for tree in l:
    for p in tree.productions():
        allproductions.append(p)# adding of rules into the list


from nltk import FreqDist
fd=FreqDist(allproductions)
print fd.hapaxes()#print the rules that are used only once
