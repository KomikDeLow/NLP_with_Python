# Iryna Brykailo, ALs-13

import nltk
from nltk.draw.tree import draw_trees
tree1 = nltk.Tree('NP', ['Mary']) # ��������� ����� ������
tree2 = nltk.Tree('NP', ['the', 'pictures']) # ��������� ����� ������
tree3 = nltk.Tree('VP', ['painted', tree2]) # ��������� ���� ������
draw_trees(tree1, tree2, tree3) # �������� �� ����� �� ��� �������� ������
