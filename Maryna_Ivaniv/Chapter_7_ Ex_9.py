Python 2.6.6 (r266:84297, Aug 24 2010, 18:46:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 2.6.6      ==== No Subprocess ====
>>> 
[[('Tall', 'NNP'), ('beautiful', 'JJ'), ('girls', 'NNS'), ('lay', 'VBP'), ('on', 'IN'), ('the', 'DT'), ('beach', 'NN'), ('and', 'CC'), ('look', 'VB'), ('on', 'IN'), ('the', 'DT'), ('blue', 'JJ'), ('sky', 'NN')]]
None
(S
  (NP Tall/JJ beautiful/JJ girls/NNS)
  lay/VBP
  on/IN
  (NP the/DT beach/NN)
  and/CC
  look/VBP
  on/IN
  (NP the/DT blue/JJ sky/NN))
>>> import nltk, re, pprint
>>> def ie_preprocess(document):
	 sentences = nltk.sent_tokenize(document) 
         sentences = [nltk.word_tokenize(sent) for sent in sentences] 
         sentences = [nltk.pos_tag(sent) for sent in sentences]

         
>>> print sentences
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print sentences
NameError: name 'sentences' is not defined
>>> import nltk, re, pprint
>>> def ie_preprocess(document):
	def ie_preprocess(document):
		 sentences = nltk.sent_tokenize(document)

		 
>>> sentences = [nltk.word_tokenize(sent) for sent in sentences]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
NameError: name 'sentences' is not defined
>>> 
[[('Tall', 'NNP'), ('beautiful', 'JJ'), ('girls', 'NNS'), ('lay', 'VBP'), ('on', 'IN'), ('the', 'DT'), ('beach', 'NN'), ('and', 'CC'), ('look', 'VB'), ('on', 'IN'), ('the', 'DT'), ('blue', 'JJ'), ('sky', 'NN')]]
None
(S
  (NP Little/JJ pretty/JJ puppy/NNS)
  sitting/VBG
  under/IN
  (NP the/DT table/NN)
  and/CC
  look/VBP
  on/IN
  (NP the/DT baby/NN))
>>> 
[[('Little', 'RB'), ('pretty', 'RB'), ('puppu', 'RB'), ('sitting', 'VBG'), ('under', 'IN'), ('the', 'DT'), ('table', 'NN'), ('and', 'CC'), ('looking', 'VBG'), ('on', 'IN'), ('the', 'DT'), ('baby', 'NN')]]
None
(S
  (NP Little/JJ pretty/JJ puppy/NNS)
  sitting/VBG
  under/IN
  (NP the/DT table/NN)
  and/CC
  looking/VBG
  on/IN
  (NP the/DT baby/NN))
>>> 
