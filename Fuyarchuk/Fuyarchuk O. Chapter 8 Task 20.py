# Olya Fuyarchuk Chapter 8 task 20

import nltk
from nltk.draw.tree import draw_trees
tree1 = nltk.Tree('NP', ['John'])
tree2 = nltk.Tree('NP', ['the', 'flowers'])
tree3 = nltk.Tree('VP', ['planted', tree2])
draw_trees(tree1, tree2, tree3) # Виводимо на екран результати трьох дерев
