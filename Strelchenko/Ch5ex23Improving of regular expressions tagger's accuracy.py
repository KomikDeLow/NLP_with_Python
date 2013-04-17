# TODO
# The precision is 0.127304731786
# If use the grammar with one rule r'.+', 'NNS' the precision is 0.13
#

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
print regexp_tagger.tag(brown_sents[5])
print regexp_tagger.evaluate(brown_tagged_sents) # evaluating tagger accuracy
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
	] # had added more regular expressions in order to improve its accuracy
regexp_tagger=nltk.RegexpTagger(patterns) 
print regexp_tagger.tag(brown_sents[5])
print regexp_tagger.evaluate(brown_tagged_sents) # looking how tagger accurace has improved


