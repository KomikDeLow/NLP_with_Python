Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.corpus import brown

>>> bigram_tagger = nltk.BigramTagger(train_sents)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bigram_tagger = nltk.BigramTagger(train_sents)
NameError: name 'train_sents' is not defined

>>> size = int(len(brown_tagged_sents)*0.9)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    size = int(len(brown_tagged_sents)*0.9)
NameError: name 'brown_tagged_sents' is not defined

>>> training=brown.tagged_sents(categories='religion')
>>> size = int(len(brown_tagged_sents) * 0.9)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    size = int(len(brown_tagged_sents) * 0.9)
NameError: name 'brown_tagged_sents' is not defined
>>> training=brown.tagged_sents(categories='religion')
>>> size = int(len(training) * 0.9)
>>> training=brown.tagged_sents(categories='religion')
>>> size = int(len(training) * 0.9)
>>> train_sents = training[:size]
>>> test_sents = training[size:]
>>> bigram_tagger = nltk.BigramTagger(train_sents)

>>> bigram_tagger.tag(brown_sents[2007])

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bigram_tagger.tag(brown_sents[2007])
NameError: name 'brown_sents' is not defined
>>> bigram_tagger.tag(test_sents[2007])

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bigram_tagger.tag(test_sents[2007])
  File "C:\Python27\lib\site-packages\nltk\util.py", line 672, in __getitem__
    raise IndexError('index out of range')
IndexError: index out of range
>>> bigram_tagger.tag(training[2007])

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bigram_tagger.tag(training[2007])
  File "C:\Python27\lib\site-packages\nltk\util.py", line 672, in __getitem__
    raise IndexError('index out of range')
IndexError: index out of range
>>> brown_sents=brown.sents()

>>> bigram_tagger.tag(brown_sents[2007])
[('Various', None), ('of', None), ('the', None), ('apartments', None), ('are', None), ('of', None), ('the', None), ('terrace', None), ('type', None), (',', None), ('being', None), ('on', None), ('the', None), ('ground', None), ('floor', None), ('so', None), ('that', None), ('entrance', None), ('is', None), ('direct', None), ('.', None)]
>>> unseen_sent = brown_sents[4203]
>>> bigram_tagger.tag(unseen_sent)
[('The', 'AT'), ('population', 'NN'), ('of', 'IN'), ('the', 'AT'), ('Congo', None), ('is', None), ('13.5', None), ('million', None), (',', None), ('divided', None), ('into', None), ('at', None), ('least', None), ('seven', None), ('major', None), ('``', None), ('culture', None), ('clusters', None), ("''", None), ('and', None), ('innumerable', None), ('tribes', None), ('speaking', None), ('400', None), ('separate', None), ('dialects', None), ('.', None)]
>>> bigram_tagger.evaluate(test_sents)
0.13702733058779484
>>> ================================ RESTART ================================
>>> #Maschakevich Khrystyna, ALs-13

>>> import nltkfrom nltk.corpus import brown
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> #Maschakevich Khrystyna, ALs-13

>>> import nltk

>>> from nltk.corpus import brown
>>> 
>>> bts=brown.tagged_sents(categories='religion')
>>> size = int(len(bts) * 0.9)

>>> train_sents = bts[:size] #split the data, training on 90% and testing on the remaining 10%
>>> test_sents = bts[size:]
>>> bigram_tagger = nltk.BigramTagger(train_sents)
>>> brown_sents=brown.sents() # Create variable, which was appropriated sentences from corpus Brown
>>> bigram_tagger.tag(brown_sents[2006])
[('Ultimately', None), ('the', None), ('development', None), ('will', None), ('comprise', None), ('300', None), ('units', None), (',', None), ('in', None), ('two-story', None), ('and', None), ('three-story', None), ('structures', None), ('.', None)]
>>> unseen_sent = brown_sents[4207]
>>> bigram_tagger.tag(unseen_sent)
[('To', 'TO'), ('make', 'VB'), ('one', 'PN'), ('nation', None), ('out', None), ('of', None), ('these', None), ('disparities', None), ('would', None), ('be', None), ('a', None), ('problem', None), ('large', None), ('enough', None), ('in', None), ('any', None), ('case', None), (';', None), (';', None)]
>>> bigram_tagger.evaluate(test_sents)
0.13702733058779484
>>> bigram_tagger.evaluate(train_sents)
0.7545469396645611
>>> 
