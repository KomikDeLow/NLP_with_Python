# TODO
# Lines should be less than 80 characters long
#

import nltk
from nltk.corpus import brown
sent1=nltk.word_tokenize("Go away!")
nltk.pos_tag(sent1)
#Hensirovska_Khrystyna.���� � �������� ���������� ������� �������,�� �������� ���������,�� ����� GO  � ������ Go away! �������� �� ������� ���� �������.�� ���������� ���������� ������� ����,�� ����� GO � 䳺������.
sent2=nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(sent2)
#��������� ���������� ������� �������,�������� ���������,�� ����� went � 䳺������ �������� ����.
print nltk.pos_tag(sent1)
print nltk.pos_tag(sent2)
#������ ����������,����� ������� ��������,
#�� ����� go �� went ����� ���������� ��������,����
#���� �� ������ ����� ���������� ������� �� ���������.
#��� �� ����� � ��� ���� �������� �� ������������ ���������
#�������.
