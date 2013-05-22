#Ros Iryna, PRLs-11, chapter7, exersise 9
#
#Here we investigate that words sometimes could be incorrectly tagged.
#But we could cope with it with help of good chunker. And we create
#a chunker which define Noun Phrases correctly.
#
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

