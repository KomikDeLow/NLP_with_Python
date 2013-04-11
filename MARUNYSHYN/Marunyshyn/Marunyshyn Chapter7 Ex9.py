#Irena marunyshyn PRLs-12 Chapter 7 EX 9
import nltk,re, pprint
def ie_preprocess(document):
	sentences = nltk.sent_tokenize(document)# default sentence segmenter
	sentences = [nltk.word_tokenize(sent) for sent in sentences] # word tokenizer
	sentences = [nltk.pos_tag(sent) for sent in sentences]# part-of-speech tagger
	print sentences
	
document = "Rapunze let down her long golden hair"# example sentence
print ie_preprocess(document)
grammar = r"""
NP: {<DT|JJ|NN.*>+} # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>} # Chunk prepositions followed by NP
VP:{<VB.*><NP|PP|CLAUSE>+$}# Chunk verbs and their arguments
CLAUSE: {<NP><VP>}# Chunk NP, VP
"""
sentence =[("Rapunzel","NNP"), ("let","VBD"),("down","RP"),("her","PP$"),("long","JJ"),("golden","JJ"),("hair","NN")]
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)# run the chunker
print result# print sentence and our result is the chunked sentence
