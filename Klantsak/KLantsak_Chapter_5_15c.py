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
words_brown=brown.tagged_words()
tags_brown=[t for w,t in words_brown]
fd=nltk.FreqDist(tags_brown)
print fd.items()[:20]
