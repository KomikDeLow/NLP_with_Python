import pprint
from nltk import RegexpTagger, word_tokenize
patterns = [
        (r'(The|the|A|a|An|an)$', 'AT'),   # articles
        (r'.*able$', 'JJ'),                # adjectives
        (r'.*ness$', 'NNJ'),               # nouns formed from adjectives
        (r'.*ly$', 'RB'),                  # adverbs
        (r'.*self$', 'PRR'),               # reflexive pronoun   
        (r'.*ing$', 'VBG'),                # gerunds
        (r'.*ed$', 'VBD'),                 # simple past
        (r'.*es$', 'VBZ'),                 # 3rd singular present
        (r'.*ould$', 'MD'),                # modals
        (r'.*\'s$', 'NN$'),                # possessive nouns
        (r'.*s$', 'NNS'),                  # plural nouns
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
        (r'.*', 'NN'),                     # nouns (default)
	]
regexp_tagger = RegexpTagger(patterns)
sent = raw_input("Enter the sentence:")
pprint.pprint(regexp_tagger.tag(word_tokenize(sent)))
