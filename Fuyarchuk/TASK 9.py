# fine

import nltk
from nltk.corpus import brown
text1 = nltk.word_tokenize("Go away!")
nltk.pos_tag(text1)
text2 = nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(text2)
print  nltk.pos_tag(text1)
print  nltk.pos_tag(text2)
#�� ��������� ������������� ���������� pos_tag ���� �������� �������� ������������ ��� � �������
#� ������� � ����������� �� ������� � ��� ��������� ���.� ���� �������� ��������, �� ����� GO and WENT ��
#����� ������� ���� �� ����, �� ��� ������ ���������� ���� ����.