# TODO
# I need Python modul.
#

#����������� ��������,����-12
#����� 7,�������� 3
#Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus. Inspect
#the data and try to observe any patterns in the POS tag sequences that make up
#this kind of chunk. Develop a simple chunker using the regular expression
#chunker nltk.RegexpParser. Discuss any tag sequences that are difficult
#to chunk reliably.
#import nltk
#������������ ���������� �������,��� ������� �� ������� ����� ���� ������
#����� chunking
#sentence=[("A","DT"),("dark","JJ"),("red","JJ"),("car","NN"),("came","VBD"),
          #("to","IN"),("a","DT"),("stopt","NN"),("in","IN"),("front","NN"),
          #("of","IN"),("the","DT"),("Flynn-Fletcher","JJ"),("residence","NN"),
          #("that","WDT"),("same","JJ"),("evening","NN"),(",",","),("in","IN"),
          #("another","DT"),("demension","NN"),(".",".")]
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#��������� ������������ ��������� chunk.�� ������� ����,���� ������� ������,
#������ ��������� ������
#cp= nltk.RegexpParser(grammar)
#�������� ������������ ��������� � ��������
#result = cp.parse(sentence)
#print result
#result.draw()
#�������������� �������� ������, � ���������� ��������� ������: {<DT>?<JJ>*<NN>}.
#�� ������� ������ ���, ���� chunker ������ ���������, ���� ����� ���
#���������� ������� �����������, � � ���� ����� �������.
