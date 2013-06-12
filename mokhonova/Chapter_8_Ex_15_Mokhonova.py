#Chapter_8_Ex_15_Mokhonova
import nltk
#описую граматику
grammar1 = nltk.parse_cfg("""
	S  -> NP VP
	NP ->Det Nom | Det Nom PP | PropN
	Nom ->Adj Nom | N
	VP -> V | V NP | V NP PP | V S | V Adv N
	PP -> P NP
	PropN -> 'John' | 'Mary' | 'Lee'
	Det -> 'the' | 'a'
	Adv -> 'away'
	N -> 'man' | 'woman' | 'park' | 'dog' | 'lead' | 'telescope' | 'butterfly' | 'home'
	Adj  -> 'fierce' | 'black' |  'big' | 'European'
	V -> 'saw' | 'chased' | 'barked'  | 'disappeared' | 'said' | 'reported' | 'ran'
	P -> 'in' | 'with'
""")
#приклад речення
sent = "Lee ran away home".split()
#граматичний розбір
rd_parser = nltk.RecursiveDescentParser(grammar1)
#будую дерево для даного речення
for tree in rd_parser.nbest_parse(sent):
	print tree
