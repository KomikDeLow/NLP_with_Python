import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='news')
brown_sents=brown.sents(categories='news')
patterns= [
	(r'.*ing$','VBG'), # gerunds
	(r'.*ed$','VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # carinal numbers
	]
regexp_tagger=nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[5])
[('It', None), ('recommended', 'VBD'), ('that', None), ('Fulton', None), ('legislators', 'NNS'), ('act', None), ('``', None), ('to', None), ('have', None), ('these', None), ('laws', 'NNS'), ('studied', 'VBD'), ('and', None), ('revised', 'VBD'), ('to', None), ('the', None), ('end', None), ('of', None), ('modernizing', 'VBG'), ('and', None), ('improving', 'VBG'), ('them', None), ("''", None), ('.', None)]
regexp_tagger.evaluate(brown_tagged_sents)
0.080066431966903356
patterns = [
	(r'.*ing$','VBG'), # gerunds
	(r'.*ed$','VBD'), # simple past
	(r'.(The|the|A|a|An|an|)$', 'AT'), #articles
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*able$', 'JJ'), # adjective -able
	(r'.*ful$', 'JJ'), # adjective -ful
	(r'.*ic$', 'JJ'), # adjective -ic
	(r'.*ive$', 'JJ'), #  adjective -ive
	(r'.*less$', 'JJ'), # adjective -less
	(r'.*ous$', 'JJ'), # adjective -ous
	(r'.*ment$', 'NN'), # Noun -ment
	(r'.*ship$', 'NN'), # Noun -ship
	(r'.*dom$', 'NN'), # Noun -dom
	(r'.*tion$', 'NN'), # Noun -tion
	(r'.*ist$', 'NN'), # Noun -ist
	(r'.*ly$', 'RB'), # Adverb -ly
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # carinal numbers
	]
regexp_tagger=nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[5])
[('It', None), ('recommended', 'VBD'), ('that', None), ('Fulton', None), ('legislators', 'NNS'), ('act', None), ('``', None), ('to', None), ('have', None), ('these', None), ('laws', 'NNS'), ('studied', 'VBD'), ('and', None), ('revised', 'VBD'), ('to', None), ('the', None), ('end', None), ('of', None), ('modernizing', 'VBG'), ('and', None), ('improving', 'VBG'), ('them', None), ("''", None), ('.', 'AT')]
regexp_tagger.evaluate(brown_tagged_sents)
0.12730473178590607

