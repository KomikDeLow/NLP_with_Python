# TODO
# unexpected indent!!!
#

# Vezdenko
 import nltk
 sentence = [ ("All", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and","CC"),
	       ("supervisors","NNS"), ("arrived", "VBD"), ("at","IN"),
	       ("July", "NNP"), ("and", "CC"), ("August", "NNP")]#�������� �������
 grammar="NP:{<DT>?<PRS$>?<NN.*>+<CC><NN.*>*}"#�������� ���������� �����
 cp=nltk.RegexpParser(grammar)#�������� chunk parser � ������ �������
 result=cp.parse(sentence)#test chunk parser � ���� ������
 print result#����������� ���������
