
# ĳ����� ����� "go" � "went" �� ����� ������� ���� �����, 1-�� ������� ����������� ����, � 2-�� - ��������.

>>> cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure', simplify_tags=True))
>>> cfd['go'].keys()
['V']
>>> cfd['went'].keys()
['VD']
