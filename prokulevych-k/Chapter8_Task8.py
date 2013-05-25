#Прокулевич К. ПРЛс-11, Розділ 8, Завдання 8
#In the recursive descent parser demo, experiment with changing the sentence to
#be parsed by selecting Edit Text in the Edit menu.
import nltk
#створюємо граматику:
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")
nltk.app.rdparser()
rd_parser = nltk.RecursiveDescentParser(grammar1)
sent = 'a dog ate a telescope'.split()
for w in rd_parser.nbest_parse(sent):
    print w #виводимо синтаксичний аналіз речення

nltk.app.rdparser()
rd_parser = nltk.RecursiveDescentParser(grammar1)
sent = 'a man saw a dog'.split()
 for w in rd_parser.nbest_parse(sent):
    print w
