
# Roksolana Dyrda, AL-13
# Ch7,task 2
#Regular expression�based NP chunker
import nltk
sentence=[("Katy", "NNP"), ("draws", "VBD"), ("rain", "JJ"), ("big", "JJ"), ("clouds", "NNS"), ("on", "IN"), ("the", "DT"), ("board","NN")]
grammar = "NP: {<DT>*<JJ>*<NN.*>+}" # ��������� ��������� �������
cp = nltk.RegexpParser(grammar)#��������� chunk parser � ������������� ��������� 
result = cp.parse(sentence)#���������� chunk parser �� ������
print result
