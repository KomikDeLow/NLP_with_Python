#Ros Iryna, PRLs-11, chapter 8, exercise 25
#What is the longest sentence you
#can find? What syntactic construction(s) are responsible for such long sentences?
#The structure of sentence: S-simple sentence: S,S,CONJ S,...,S CONJ P S
import nltk
from nltk.corpus import gutenberg #Importing of gutenberg corpus
gutenberg.fileids() #Gutenberg files
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt'
, 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt',
 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt',
 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'melville-moby_dick.txtPlus1MoreFile.txt',
 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt',
 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
#The longest sentence - 93 symb.
max_len= max([len(sent) for sent in gutenberg.sents('burgess-busterbrown.txt')])
max_sent= [sent for sent in gutenberg.sents('burgess-busterbrown.txt') if len(sent)==93]
print 'max len Sent:',max_len














