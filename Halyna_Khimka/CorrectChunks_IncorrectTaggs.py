#Halyna Khimka
# Chapter 7.9
#
"""
This program shows that sometimes a word is incorrectly tagged.
But a good chunker is able to work with the erroneous output of taggers.
There are some words in the sentence that are tagged incorrectly:
'Universal' and 'Open'.
But in spite of this my chunker has defined Noun Phrases correctly.

"""
import nltk
from nltk.corpus import brown

sent="Universal Network Objects is the component model used in the Open Office computer software application suites."
sent=nltk.word_tokenize(sent)
sent=nltk.pos_tag(sent)
print sent
grammar = "NP: {<DT|AT|>?<OD>?<JJ.*>*<N.*>+}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sent)
result.draw()

