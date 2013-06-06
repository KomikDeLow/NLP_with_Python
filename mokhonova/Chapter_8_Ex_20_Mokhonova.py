# Chapter_8_Ex_20_Mokhonova
import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
# derevo 1
tree1 = nltk.Tree('NP', ['the', 'dog'])
# derevo 2
tree2 = nltk.Tree('NP', ['a', 'man'])
# derevo 3 
tree3 = nltk.Tree('VP', ['saw', tree2])
# vykorystovuju funkciju draw trees
draw_trees(tree1, tree2, tree3)

