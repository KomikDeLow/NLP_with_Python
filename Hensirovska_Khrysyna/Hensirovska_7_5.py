# TODO
# I need Python modul.
#

#����������� ��������,����-12
#����� 7,�������� 5
#Write a tag pattern to cover noun phrases that contain gerunds, e.g., the/DT
#receiving/VBG end/NN, assistant/NN managing/VBG editor/NN. Add these patterns
#to the grammar, one per line. Test your work using some tagged sentences of
#your own devising.
#import nltk
#������������ ���������� �������,��� ������� �� ������� ����� ���� ������
#����� chunking
#grammar = r"""
#������ �������,�� ����� ������� �� ������������ ������.
#���������� ����� ������� ���������� ���� chunker ������ �� ������� ����
#optional determiner(DT) ��� ������� ,���� 䳺�����(���� ����,��� ��
#���� � ����������� �����) � ���������
#NP:{<DT|NN>?<VBG><NN>}"""
#define an example sentence to be chunked
#sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","),
           # ("assistant","NN"),("managing","VBG"),("editor","NN")]
#��������� ������������ ��������� chunk.�� ������� ����,���� �������
#������,������ ��������� ������
#cp = nltk.RegexpParser(grammar)
#run the chunker on this input
#print cp.parse(sentence)
#sentence= [("A","DT"),("dark","JJ"),("red","JJ"),("car","NN"),
          # ("came","VBD"),("to","IN"),("a","DT"),("stopt","NN"),("in","IN"),
           #("front","NN"),("of","IN"),("the","DT"),("Flynn-Fletcher","JJ"),
           #("residence","NN"),("that","WDT"),("same","JJ"),("evening","NN"),
           #(",",","),("in","IN"),("another","DT"),("demension","NN"),(".",".")]
#��������� ������������ ��������� chunk.�� ������� ����,���� ������� ������,
#������� �������� ����������� ������
#cp= nltk.RegexpParser(grammar)
#run the chunker on this input
#print cp.parse(sentence)
