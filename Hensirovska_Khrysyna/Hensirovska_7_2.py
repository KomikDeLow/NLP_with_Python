#����������� ��������,����-12
#����� 7,�������� 2
#Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
#to do this by generalizing the tag pattern that handled singular noun phrases.
#import nltk
#sentence = [("many", "JJ"), ("researches", "NNS"),(",", ","), ("two", "CD"),
           # ("weeks", "NNS"),(",", ","), ("both", "DT"), ("new", "JJ"),
           # ("positions", "NNS")]
#������������ ���������� �������,��� ������� �� ������� ����� ���� ������
#����� chunking
#grammar = "NP: {<DT|CD>?<JJ>*<NN.>}"
#��������� ������������ ��������� chunk.�� ������� ����,���� ������� ������,
#������ ��������� ������
#cp = nltk.RegexpParser(grammar)
#�������� ������������ ��������� � ��������
#result = cp.parse(sentence)
#print result
#result.draw()
#�� ������� �������� ��������� ������, �� ��������� � ���� �������� �������.
