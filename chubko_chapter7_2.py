# Chubko Uliana AL-12
# ������� ���� ��� ���������� �������� � ������
import nltk
from nltk import *
tagged_tokens = [("happy ", "JJ"), ("writers","NNS"),("five", "CD"),("days", "NNS"), ("interesting","JJ"),("positions","NNS"),("tall","JJ"),("bull","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|>?<JJ.*>?<NNS>+}")
print cp.parse(tagged_tokens)
# ������� ����, ��� ����������� �������� � �����
tagged_tokens_singular = [("happy ", "JJ"), ("writers","NNS"),("five", "CD"),("days", "NNS"), ("interesting","JJ"),("positions","NNS"),("tall","JJ"),("bull","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|>?<JJ.*>?<NN>+}")
print cp.parse(tagged_tokens_singular)
# ������� ���� ��� ���������� �������� �� � �����, ��� � � ������
tagged_tokens_singular_plural = [("happy ", "JJ"), ("writers","NNS"),("five", "CD"),("days", "NNS"), ("interesting","JJ"),("positions","NNS"),("tall","JJ"),("bull","NN")]
cp = nltk.RegexpParser("NP: {<DT|CD|PP\$|JJ.*|VBG>?<JJ.*>?<NN.*>+}")
print cp.parse(tagged_tokens_singular_plural)
