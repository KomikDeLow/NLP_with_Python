# Andrew Melnyk ALs-12

import nltk
from nltk.corpus import brown
taggedw=brown.tagged_words() # ǳ ��� ������� Brown �������� � � ���� ���� ����������� � NN � ������ ��������� �����
tags=[t for w,t in taggedw if t.startswith('NN')] 
fd=nltk.FreqDist(tags)
fd.items()[10:]
