#Прокулевич К. ПРЛс-11, Розділ 5, Задача 28
#Experiment with taggers using the simplified tagset (or make one of your own
#by discarding all but the first character of each tag name).
import nltk
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
[word+"/" + tag for (word, tag) in word_tag_fd if tag.startswith ('N')] [:30]#find the most common nouns in the news
#category of the BrownCorpus
#find the most common verbs:
wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')] [:30]
#A simplified tagset has less information about context and
#has a smaller range of choices in classifying the current token.
