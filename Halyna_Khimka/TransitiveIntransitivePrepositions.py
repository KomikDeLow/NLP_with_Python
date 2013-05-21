# Halyna Khimka
# Chapter 8.15
# Extend the grammar in grammar2 with productions that expand prepositions as
# intransitive, transitive, and requiring a PP complement. Based on these productions,
# use the method of the preceding exercise to draw a tree for the sentence Lee
# ran away home.
#
#
"""
Intransitive prepositions do not take an object. For example Run off doesn't take an object. It is a particle.
Transitive prepositions require an object (NP, VP, S OR PP complements).
For example Run Away Home: Away requires an object. Run away is not phrasal verb.
Sometimes prepositions require PP complement. For example Run Away From Angry Squirrel.


"""

import nltk
from nltk import tree

grammar2 = nltk.parse_cfg("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP | V PP | V P
PP -> P NP | P N | P P N | P P 
PropN -> 'Buster' | 'Chatterer' | 'Joe' | 'Lee'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log' | 'home'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put' | 'ran'
P -> 'on' | 'away' | 'from'| 'with' | 'off'
""")

sent="Lee ran away home".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.nbest_parse(sent):
    print tree.draw()
