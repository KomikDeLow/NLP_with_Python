

import nltk
# ��������� corpus treebank
from nltk.corpus import treebank 
# ������ �� ����������� ���������� �������
tree = treebank.parsed_sents('wsj_0005.mrg')[1]
print 'Tree = ', tree
#�������� ������� � ������
tree.productions()
freqdist = nltk.FreqDist(tree.productions())
print freqdist
