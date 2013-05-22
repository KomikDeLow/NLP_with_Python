Python 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 2.6.6      
>>> import nltk
from nltk.corpus import brown
taggedw=brown.tagged_words() 
tags=[t for w,t in taggedw if t.startswith('NN')]
fd=nltk.FreqDist(tags)
print fd.items()[10:]

# This tags are simple tags with modifiers.
# Each tag consists of a base tag and optional modifiers.
# The modifiers include multiple tags separated by plus-signs (eg. EX+BEZ),
# multiple tags concatenated in the case of negation (eg. BEZ*),
# the prefix modifier FW- for foreign words (e.g. FW-JJ),
# the suffix modifier -NC for citations (e.g. NN-NC),
# the suffix -HL for words in headlines (e.g. NN-HL-TL in titles (e.g. NNS-TL).
