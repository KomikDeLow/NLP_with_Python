# fine
# Fuyarchuk O. Chapter 8 Task 25
# The structure of sentence: S-simple sentence: S,S,CONJ S,...,S CONJ P S
import nltk
from nltk.corpus import gutenberg # імпортуємо корпус gutenberg
gutenberg.fileids() # файли корпуса gutenberg
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt'
, 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt',
 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt',
 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'melville-moby_dick.txtPlus1MoreFile.txt',
 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt',
 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
#Знаходимо довжину  найдовшого речення
max_len= max([len(sent) for sent in gutenberg.sents('burgess-busterbrown.txt')])
#Виводимо найдовше речення,яке має довжину 93 символи
max_sent= [sent for sent in gutenberg.sents('burgess-busterbrown.txt') if len(sent)==93]
print 'max len Sent:',max_len














