import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='news')
brown_sents=brown.sents(categories='news')
patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
        (r'.*', 'NN') # nouns (default)
        ]
regexp_tagger=nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print('������� ����������')
print(regexp_tagger.evaluate(brown_tagged_sents))
patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
        (r'(The|the|A|a|An|an|)$', 'AT'), #articles
	(r'.*es$', 'VBZ'), # 3rd singular present
        (r'.*able$', 'JJ'), # adjective -able
        (r'.*ful$', 'JJ'), # adjective -ful
        (r'.*ic$', 'JJ'), # adjective -ic
        (r'.*ive$', 'JJ'), # adjective -ive
        (r'.*less$', 'JJ'), # adjective -less
        (r'.*ous$', 'JJ'), # adjective -ous
        (r'.*ment$', 'NN'), # adjective -ment
        (r'.*ship$', 'NN'), # adjective -ship
        (r'.*dom$', 'NN'), # adjective -dom
        (r'.*tion$', 'NN'), # adjective -tion
        (r'.*ist$', 'NN'), # adjective -ist
        (r'.*ly$', 'RB'), # adjective -ly
        (r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
        (r'.*', 'NN') # nouns (default)
        ]
regexp_tagger=nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print('������� ����������')
print(regexp_tagger.evaluate(brown_tagged_sents))
#������� ����������, ���� ��� ������� � ���������, ������ 20%.
#ϳ��� ����, �� ������ � ��������� ��� �������, ���� ����������� ������ �� 30%.
#������� evaluate �������� ��� �������� ������� ����������
#��� �������� � ��������� �����������, �� ��� �� ����� ������ �������
#������������� ����������. 
#��� �������� ��������, ����� accurate() �� ������� �����������.  �������� �������. 
#�������� ��������������� ������� evaluate.
