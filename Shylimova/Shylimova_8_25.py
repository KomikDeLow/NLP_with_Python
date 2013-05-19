# Shylimova K. Al-13
# Chapter 8, task 25
# Download several electronic books from Project Gutenberg.
# Scan these texts for any extremely long sentences.
# The longest sentence I can find.
# Syntactic constructions, that are responsible for such long sentences, (I replace simple sentenses with S) are:
# S preposition(PP) S, S wh determiner(WH) S, S gerund(VBG) S

import nltk
from nltk.corpus import gutenberg
print 'Тексти в корпусі= ', gutenberg.fileids()
hamlet = gutenberg.sents('shakespeare-hamlet.txt')
print 'Речення з тексту Гамлет= ', hamlet
print 'Кількість речень у Гамлеті= ', len(hamlet)
print '1234 речення= ',hamlet[1234]
najdovshe = max([len(rechennja) for rechennja in hamlet])
print 'Найдовше речення в Гамлеті= ', [rechennja for rechennja in hamlet if len(rechennja) == najdovshe]
print 'Кількість слів у реченні= ', najdovshe
texts = gutenberg.sents()
print 'Речення з корпусу= ', texts
print 'Кількість речень у корпусі= ', len(texts)
najdovshe = max([len(rechennja) for rechennja in texts])
print 'Найдовше речення в корпусі= ', [rechennja for rechennja in texts if len(rechennja) == najdovshe]
print 'Кількість слів у реченні= ', najdovshe
