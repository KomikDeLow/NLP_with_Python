# TODO
# It isn't the Python modul
#
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> fd = nltk.FreqDist()
>>> text3=nltk.corpus.brown.words(categories='a')
>>> dic=['']
>>> for (wd, tg) in nltk.corpus.brown.tagged_words():
if tg[:2] == 'QL':
fd.inc(wd + "/" + tg) 
>>> fd.sorted()[:30]
['as/QL', 'more/QL', 'so/QL', 'very/QL', 'most/QL', 'too/QL', 'enough/QLP', 'much/QL', 'quite/QL', 'less/QL', 'all/QL', 'almost/QL', 'no/QL', 'far/QL', 'right/QL', 'even/QL', 'little/QL', 'rather/QL', 'somewhat/QL', 'highly/QL', 'relatively/QL', 'well/QL', 'All/QL', 'pretty/QL', 'just/QL', 'As/QL', 'that/QL', 'fairly/QL', 'really/QL', 'completely/QL']
>>> verbs=['adore', 'love', 'like', 'prefer']
>>> for (wd, tg) in nltk.corpus.brown.tagged_words():
if tg[:2] == 'QL':
fd.inc(wd) 
>>> fd.sorted()[:30]
['as/QL', 'as', 'more', 'more/QL', 'so', 'so/QL', 'very', 'very/QL', 'most', 'most/QL', 'too', 'too/QL', 'enough', 'enough/QLP', 'much', 'much/QL', 'quite', 'quite/QL', 'less', 'less/QL', 'all', 'all/QL', 'almost', 'almost/QL', 'no/QL', 'no', 'far/QL', 'far', 'right/QL', 'right']
>>> for i in range(len(text3)):
if text3[i]in fd.sorted()and text3[i+1]in verbs and (text3[i]+' '+text3[i+1]) not in dic:
dic.append(text3[i]+' '+text3[i+1])

>>> dic
['just like', 'always like', 'to like', 'to love', 'little love', 'that love', 'somewhat like', 'more like', 'increasingly like', 'sound like', 'much like', 'just love', 'quite like', 'generally prefer', 'exactly like', 'great love', 'much prefer', 'roughly like', 'this love', 'to prefer', 'so like', 'as love', 'all love', 'that like']
