# Shylimova K. Al-13
# Chapter 8, task 25
# Download several electronic books from Project Gutenberg.
# Scan these texts for any extremely long sentences.
# The longest sentence I can find.
# Syntactic constructions, that are responsible for such long sentences, (I replace simple sentenses with S) are:
# S preposition(PP) S, S wh determiner(WH) S, S gerund(VBG) S

import nltk
from nltk.corpus import gutenberg
print '������ � ������= ', gutenberg.fileids()
hamlet = gutenberg.sents('shakespeare-hamlet.txt')
print '������� � ������ ������= ', hamlet
print 'ʳ������ ������ � ������= ', len(hamlet)
print '1234 �������= ',hamlet[1234]
najdovshe = max([len(rechennja) for rechennja in hamlet])
print '�������� ������� � ������= ', [rechennja for rechennja in hamlet if len(rechennja) == najdovshe]
print 'ʳ������ ��� � ������= ', najdovshe
texts = gutenberg.sents()
print '������� � �������= ', texts
print 'ʳ������ ������ � ������= ', len(texts)
najdovshe = max([len(rechennja) for rechennja in texts])
print '�������� ������� � ������= ', [rechennja for rechennja in texts if len(rechennja) == najdovshe]
print 'ʳ������ ��� � ������= ', najdovshe
