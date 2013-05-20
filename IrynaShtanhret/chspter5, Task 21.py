# TODO
# Only 'adore' and 'prefer' are always a verb. 
# 'love' and 'like' are noun/adj...
#

#����� �������� ����-13
import nltk
from nltk.corpus import brown
text=nltk.corpus.brown.words(categories='romance') #��������� ������ � ���������� �� ������� � ������� Brown
dic=[]
fs=[]
verbs=['adore', 'love', 'like', 'prefer'] #�������� ��� ������� ������ �� ������ �� ������� � �����
for (wd,tg) in nltk.corpus.brown.tagged_words():
	if tg[:2]=='QL':
		fs.append(wd)
fs[:20]
['well', 'less', 'very', 'most', 'so', 'real', 'less', 'most', 'as', 'highly', 'fundamentally', 'even', 'very', 'as', 'very', 'most', 'how', 'mighty', 'most', 'much']
#��������� �������� ������ ������� ���� ���� � QL
for i in range(len(text)):
	if text[i]in fs and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
		dic.append(text[i]+' '+text[i+1])
	
dic
['just like', 'exactly like', 'real love', 'sound like', 'that love', 'Just like', 'plain like', 'much like', 'even like', 'only love', 'always love', 'to love', 'this love', 'little like', 'rather like']
 
