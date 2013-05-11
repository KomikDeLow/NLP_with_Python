import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='news')
brown_sents=brown.sents(categories='news')
input_data=[
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
	(r'.*', 'NN') # nouns (default)
 ]
regexp_tagger = nltk.RegexpTagger(input_data)
regexp_tagger.tag(brown_sents[4])
print regexp_tagger.evaluate(brown_tagged_sents)
#Для покращення результату нам потрібно поєднати даний Tagger з Default Tagger


