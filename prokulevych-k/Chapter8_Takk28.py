# Прокулевич К. ПРЛс-11, Розділ 8, завдання 28
# Process each tree of the Penn Treebank Corpus sample nltk.corpus.treebank
#and extract the productions with the help of Tree.productions(). Discard the productions
#that occur only once. Productions with the same lefthand side and similar
#righthand sides can be collapsed, resulting in an equivalent but more compact set
#of rules. Write code to output a compact grammar.
import nltk
from nltk.corpus import treebank #import corpus treebank
tree = treebank.parsed_sents('wsj_0005.mrg')[1]# доступ до синтаксично розміченого речення
print 'Tree = ', tree
tree.productions()#виписуємо правила з дерева
freqdist = nltk.FreqDist(tree.productions())
print freqdist
