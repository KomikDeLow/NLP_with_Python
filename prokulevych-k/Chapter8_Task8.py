#���������� �. ����-11, ����� 8, �������� 8
#In the recursive descent parser demo, experiment with changing the sentence to
#be parsed by selecting Edit Text in the Edit menu.
import nltk
#��������� ���������:
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
    print w #�������� ������������ ����� �������

nltk.app.rdparser()
rd_parser = nltk.RecursiveDescentParser(grammar1)
sent = 'a man saw a dog'.split()
 for w in rd_parser.nbest_parse(sent):
    print w
