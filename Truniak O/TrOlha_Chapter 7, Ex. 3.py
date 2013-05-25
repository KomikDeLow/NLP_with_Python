# Presented by Olha Truniak, ALs-13
# Chapter 7, Ex. 3

# Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus. Inspect
# the data and try to observe any patterns in the POS tag sequences that make up
# this kind of chunk. Develop a simple chunker using the regular expression chunker
# nltk.RegexpParser. Discuss any tag sequences that are difficult to chunk reliably.

import nltk
"""I chose to study the verb phrase.
   Before you write the rules for the allocation of this type of
   expression I watched the expressions marked the first ten sentences of corpus:"""
example = nltk.corpus.conll2000.chunked_sents('train.txt')[:10]
def chunked_tags(train): 
	    """Generate a list of tags that tend to appear inside chunks"""
	    cfdist = nltk.ConditionalFreqDist()
	    for t in train:
	        for word, tag, chtag in nltk.chunk.tree2conlltags(t):
	            if chtag == "O":
	                cfdist[tag].inc(False)
	            else:
	                cfdist[tag].inc(True)
	    return [tag for tag in cfdist.conditions() if cfdist[tag].max() == True]

train_sents = nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('VP',))
print chunked_tags(train_sents)
# Then wrote a program for the selection of verbal expressions in the corpus:
example = nltk.corpus.conll2000.chunked_sents('train.txt')[0]
cp = nltk.RegexpParser(r"""
	  VP: {<MD><VB>*} # verb phrase chunks     
	      {<VB.*>?<RB>?<VB.*>+<TO><VB.*>+}
	      {<TO>?<VB.*>+}  
	  """)

print cp.parse(example.flatten(), trace=1)

