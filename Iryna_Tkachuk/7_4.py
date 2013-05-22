#Presented by Tkachuk Iryna

"""7_4  An early definition of chunk was the material that occurs between chinks.
Develop a chunker that starts by putting the whole sentence in a single chunk,
and then does the rest of its work solely by chinking. Determine which tags
(or tag sequences) are most likely to make up chinks with the help of your own
utility program. Compare the performance and simplicity of this approach
relative to a chunker based entirely on chunk rules."""


import nltk
#some sentence
sentence = [("Sumsung", "NNP"), ("is", "VBZ"), ("the", "DT"),
            ("leader", "NN"), ("in", "IN"), ("mobile", "JJ"),
            ("technology", "NN")] 
#define grammar, at first chunk everything and then chink
grammar = r"""
NP:
	{<.*>+}
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)  #create a chunk parser
result = cp.parse(sentence)    #present result
print result

