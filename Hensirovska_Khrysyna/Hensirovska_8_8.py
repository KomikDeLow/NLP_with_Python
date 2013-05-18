# TODO
# I need Python modul.
#


#Генсіровська Христина,ПРЛс-12
#Розділ 8,завдання 8
#In the recursive descent parser demo, experiment with changing the sentence to
#be parsed by selecting Edit Text in the Edit menu.
import nltk
#встановлюємо просту граматику
grammar1 = nltk.parse_cfg("""
#S -> NP VP
#VP -> V NP | V NP PP
#PP -> P NP
#V -> "saw" | "ate" | "walked"
#NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
#Det -> "a" | "an" | "the" | "my"
#N -> "man" | "dog" | "cat" | "telescope" | "park"
#P -> "in" | "on" | "by" | "with"
#""")
rd_parser = nltk.RecursiveDescentParser(grammar1)#програма синтаксичного аналізу
sent = 'Mary saw a dog'.split()#створили речення
for t in rd_parser.nbest_parse(sent):
	print t #виводимо на екран синтаксичний аналіз
sent = 'John ate a cat'.split() #змінили речення

for t in rd_parser.nbest_parse(sent):
	print t #виводимо на екран синтаксичний аналіз

sent = 'Bob saw a telescope'.split() #експериментуємо створивши ще одне речення
for t in rd_parser.nbest_parse(sent):
  print t

sent = 'Mary saw Bob with a cat'.split() #змінюємо речення
for t in rd_parser.nbest_parse(sent):
	print t

sent = 'Mary saw Bob with a cat in the park'.split() #додаємо до речення нові
#слова
for t in rd_parser.nbest_parse(sent):
	print t
#Отже,бачимо,що recursive descent parser подає кожне речення як вузол поклада-
#ючись на встановлену нами граматику,яка шукає елементи,що можуть використову-
#ватись для збільшення дерева.Основною  метою recursive descent parser є знайти
#іменниковий вираз,а потім дієслівний.
