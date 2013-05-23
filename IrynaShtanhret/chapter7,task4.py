#Iryna Shtanhret, AL-13, Task4, Chapter 7
#��������� ����������  chunk (���� �����) - �������, ���� ����������� �� �����������.
#������� Chunker, �� ����������  � ������� � ������ �����(chunk), ����� ������ ��������� �������� ������ ���������� ��������.
#��������, �� ���� (��� ����������� ����), ���������� ��������� ���������  �� ��������� ���� ������ ��������� ��������.
#�������� ������������� � ���������� ������ ������ �������� � ���������-�������������� ������� ��������� �� �������� �����(chunk).

import nltk
#some sentence
sentence = [("Apple", "NNP"), ("is", "VBZ"), ("the", "DT"),
            ("leader", "NN"), ("in", "IN"), ("computer", "JJ"),
            ("technology", "NN")] 
#define grammar, at first chunk everything and then chink
grammar = r"""
NP:
	{<.*>+}
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)  #create a chunk parser
result = cp.parse(sentence)    #present result
print result
