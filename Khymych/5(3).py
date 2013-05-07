Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> text = nltk.word_tokenize("They wind back the clock, while we chase after the wind")
>>> nltk.pos_tag(text)
[('They', 'PRP'), ('wind', 'VBP'), ('back', 'RB'), ('the', 'DT'), ('clock', 'NN'), (',', ','), ('while', 'IN'), ('we', 'PRP'), ('chase', 'VBP'), ('after', 'IN'), ('the', 'DT'), ('wind', 'NN')] #Here we see that They and we are PRP, pronouns; wind and chase are VBP, verbs in the Present Simple tense; back is RB, an adverb; the is DT, a Determiner; clock and wind are NN, nouns; while and after are IN, prepositions.
#In the first instance WIND  /waind/ is a verb, in the second /wind/ is a noun. The difference in pronounciation between the two words is that /waind/ features a long vowel, while /wind/ uses a short vowel.
>>> 
