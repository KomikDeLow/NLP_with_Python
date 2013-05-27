# bad
# Roman Borys PRLs-11
import nltk
from nltk.corpus import brown
verbs=['adore', 'love', 'like', 'prefer'] #checking for words
text=nltk.corpus.brown.tagged_words(categories='news') 
#Assigning variable text all the words, that belong to brown corpus
#news category
a=[w for w in nltk.bigrams(text) if w[0][1].startswith
('QL') and w[1][1].startswith('V')]
a
#showing the result on the screen
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
a
text=nltk.corpus.brown.tagged_words(categories='romance')
#Assigning variable text all the words, that belong to brown corpus
#romance category
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
text=nltk.corpus.brown.tagged_words(categories='religion')
#Assigning variable text all the words, that belong to brown corpus
#religion category
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
text=nltk.corpus.brown.tagged_words(categories='news')
#checking if the process is done correctly
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0]=='operated']


