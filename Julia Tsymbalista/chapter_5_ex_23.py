# Iuliia Tsymbalista ALs-13
# chapter 5, ex. 23
# Consider the regular expression tagger developed in the exercises in the previous
#section. Evaluate the tagger using its accuracy() method, and try to come up with
#ways to improve its performance.


import nltk
from nltk.corpus import brown
patterns = [
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNS'), # plural nouns
    (r'.*', 'NN'), # nouns (default)
    (r'.*er', 'JJR'),	# adjective, comparative
    (r'.*est', 'JJT'),	# adjective, superlative
    (r'.*ly', 'JJT'),	# adverb
    (r'.*dom', 'NNC'),	# noun, singular,collective
    (r"NP: {<[CDJNP].*>+}"), #rules for typical noun phrase
     ]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown.sents()[15])
brown_test=brown.tagged_sents()[:150]
print 'RegexpTagger:'
print 'Accuracy:', regexp_tagger.evaluate(brown.tagged_sents()[150:1000])

# for higher accuracy I use unigram,bigram and trigram taggers with the RegexpTagger
unigram_chunker = nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
bigram_chunker = nltk.BigramTagger(brown_test, backoff=unigram_chunker)
trigram_chunker=nltk.TrigramTagger(brown_test, backoff=bigram_chunker)
print 'RegexpTagger + Trigram tagger:'
print 'Accuracy:', trigram_chunker.evaluate(brown.tagged_sents()[150:1000])
