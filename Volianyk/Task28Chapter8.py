

import nltk
# імпортуємо corpus treebank
from nltk.corpus import treebank 
# доступ до синтаксично розміченого речення
tree = treebank.parsed_sents('wsj_0005.mrg')[1]
print 'Tree = ', tree
#виписуємо правила з дерева
tree.productions()
freqdist = nltk.FreqDist(tree.productions())
print freqdist
