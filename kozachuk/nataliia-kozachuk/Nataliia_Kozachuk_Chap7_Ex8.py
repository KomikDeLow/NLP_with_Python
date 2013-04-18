#Nataliia Kozachuk,PRLs-12
#Chapter 7, Ex8

import nltk
grammar = """
NP:
{<DT>?<JJ>*<NN>*<NNS>*}
}<VBP|IN>+{
"""
cp=nltk.RegexpParser(grammar)
sentence=[('Tall','JJ'),('charming','JJ'),('girls','NNS'),('laugh','VBP'),('on','IN'),('the','DT'),('bench','NN'),('and','CC'),('look','VBP'),('on','IN'),('the','DT'),('clear','JJ'),('river','NN')]
print cp.parse(sentence)
#stvoryemo gramatuky
#Chunk sequences of deterniner, adjectives,noun,noun plural
#Chink sequences of present verb and preposition
#create a chunk perser
#Test chunk parser in the senntence
#rusults of our program
