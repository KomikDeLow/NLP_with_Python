#Chubko Uliana AL-12
import nltk
from nltk import *
# побудувати граматику для речення "John goes home"
grammar1 = nltk.parse_cfg("""
S  -> NP VP
NP -> DET N PP
VP -> V NP
V -> "goes" 
NP -> "John"  
NP ->  "home" 
""")
sent_1 = "John goes home".split()
rd_parser_1 = nltk.RecursiveDescentParser(grammar1)
for tree_1 in rd_parser_1.nbest_parse(sent_1):
    print tree_1
tree_1.draw()
# заміна першого розширення:
grammar1 = nltk.parse_cfg("""
S  -> NP VP
NP -> NP PP
VP -> V NP
V -> "goes" 
NP -> "John"  
NP ->  "home" 
""")
sent = "John goes home".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
    print tree
tree.draw()
# бачимо,що вибиває помилку:
File "C:\Python26\lib\site-packages\nltk\tree.py", line 138, in __getitem__
#if isinstance(index, (int, slice)):
#RuntimeError: maximum recursion depth exceeded in __instancecheck__
