import nltk
fd = nltk.FreqDist()
text=nltk.corpus.brown.words(categories='romance')
dic=['']
for (wd, tg) in nltk.corpus.brown.tagged_words():
	if tg[:2] == 'QL':
		fd.inc(wd + "=" + tg)
for (wd, tg) in nltk.corpus.brown.tagged_words():
	if tg[:2] == 'QL':
		fd.inc(wd)
verbs=['adore', 'love', 'like', 'prefer']
for i in range(len(text)):
	if text[i]in fd.keys()and text[i+1]in verbs and (text[i]+' '+text[i+1]) not in dic:
		dic.append(text[i]+' '+text[i+1])

print dic
