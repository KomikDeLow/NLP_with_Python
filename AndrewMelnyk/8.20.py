# TODO
# � ������ �� �������������

# Andrew Melnyk ALs-12

import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
# 1 ������
tree1 = nltk.Tree('NP', ['the', 'dog'])
# 2 ������
tree2 = nltk.Tree('NP', ['a', 'man'])
# 3 ������
tree3 = nltk.Tree('VP', ['saw', tree2])
# ������������ �-� draw_trees()
draw_trees(tree1, tree2, tree3)

