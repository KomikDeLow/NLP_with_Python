#Khrystyna Hensirovska unit 5 ex.18
#Generate some statistics for tagged data to answer the following questions:
#a. What proportion of word types are always assigned the same part-of-speech
#tag?
#b. How many words are ambiguous, in the sense that they appear with at least
#two tags?
#c. What percentage of word tokens in the Brown Corpus involve these ambiguous
#words?
import nltk
from nltk.corpus import brown
tags=brown.tagged_words(simplify_tags=True)#������������� ����� tagged_words,
#��� �������� ����������� �������
base=nltk.ConditionalFreqDist((word.lower(), tag)
			      for (word, tag) in tags)

for word in base.conditions():
	if len(base[word]) > 3:
		tags = base[word].keys()
		print word, ' '.join(tags)#��������� ����������� �����,������-
		#��� �� �������� � �����,��� �������� ���������� �� �����-
		#�������� ������
		a=len(brown.words())
b=len(base.conditions())
procent=b/a
procent #��������� ������� ������������� ���
