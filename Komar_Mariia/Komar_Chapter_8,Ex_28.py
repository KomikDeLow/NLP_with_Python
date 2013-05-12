# TODO
# Process each tree !
#

#Komar Mariia Als-11
#Chapter8_ Ex_28

#Process each tree of the Penn Treebank Corpus sample nltk.corpus.treebank
#and extract the productions with the help of Tree.productions().
#Discard the productions that occur only once. Productions with the same
#lefthand side and similar righthand sides can be collapsed, resulting in
#an equivalent but more compact set of rules. Write code to output a compact
#grammar.

import nltk
from nltk.corpus import treebank #import corpus treebank
tree = treebank.parsed_sents('wsj_0005.mrg')[0] #отримуємо доступ до синтаксично розміченого речення
print 'Tree = ', tree #виводмо речення у вигляді дерева
tree.productions() #виписуємо всі правила з цього дерева
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys() #формуємо список правил
print '  Grammar = '
for i in freqdist.keys():
	if freqdist[i]>=1:
		print '          ', i
		
