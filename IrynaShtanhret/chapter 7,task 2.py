# -*- coding: cp1251 -*-
#Iryna Shtanhret, Al-13, Task 2, Chapter 7
#���������� ��������� ������, �� ������ �������� �������, ���������,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS .
#������� �������� ���������� ����� �� ��������� ������������ ������� ,��  �������� ��������� ������ ������.
import nltk
sentence = [("many", "JJ"), ("researchers","NNS"), ("two","CD"),("weeks","NNS"), ("both","DT"),("new","JJ"),("positions","NNS")]
grammar="NP:{<DT|CD>?<JJ>*<NN.>}"
cp=nltk.RegexpParser(grammar)
result=cp.parse(sentence)
print result
