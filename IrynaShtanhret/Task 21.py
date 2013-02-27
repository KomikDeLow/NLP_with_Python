#Ірина Штангрет ПРЛс-13
import nltk
from nltk.corpus import brown
text=nltk.corpus.brown.words(categories='romance') #Створюємо змінну і заповнюємо її словами з корпусу Brown
dic=[]
fs=[]
verbs=['adore', 'love', 'like', 'prefer'] #Створили дві порожні змінні та змінну зі словами з умови
for (wd,tg) in nltk.corpus.brown.tagged_words():
	if tg[:2]=='QL':
		fs.append(wd)
fs[:20]
['well', 'less', 'very', 'most', 'so', 'real', 'less', 'most', 'as', 'highly', 'fundamentally', 'even', 'very', 'as', 'very', 'most', 'how', 'mighty', 'most', 'much']
#Заповнили порожній список словами теги яких є QL
for i in range(len(text)):
	if text[i]in fs and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
		dic.append(text[i]+' '+text[i+1])
	
dic
['just like', 'exactly like', 'real love', 'sound like', 'that love', 'Just like', 'plain like', 'much like', 'even like', 'only love', 'always love', 'to love', 'this love', 'little like', 'rather like']
 
