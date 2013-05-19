# Shylimova K. Al-13
# Chapter 5 task 22
# Enter test sentence: She was invited by her Royal Highness herself.

import pprint
from nltk import RegexpTagger, word_tokenize
patterns = [
	#Custom rules
        (r'(The|the|A|a|An|an)$', 'AT'),   # articles
        (r'.*able$', 'JJ'),                # adjectives
        (r'.*ness$', 'NNJ'),               # nouns formed from adjectives
        (r'.*ly$', 'RB'),                  # adverbs
        (r'.*self$', 'PRR'),               # reflexive pronoun
            
        #Default rules from task
        (r'.*ing$', 'VBG'),              # gerunds
        (r'.*ed$', 'VBD'),               # simple past
        (r'.*es$', 'VBZ'),               # 3rd singular present
        (r'.*ould$', 'MD'),              # modals
        (r'.*\'s$', 'NN$'),              # possessive nouns
        (r'.*s$', 'NNS'),                # plural nouns
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
        (r'.*', 'NN'),                   # nouns (default)
	]

regexp_tagger = RegexpTagger(patterns)
sentence = raw_input("Enter test sentence:\n")
pprint.pprint(regexp_tagger.tag(word_tokenize(sentence)))
