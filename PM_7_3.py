import nltk
# using the NLTK corpus module to access a larger amount of chunked text
from nltk.corpus import conll2000 
print conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99]

# noun phrase chunking with a unigram tagger (a constructor method)
class UnigramChunker(nltk.ChunkParserI):
	def __init__(self, train_sents):
		train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
			      for sent in train_sents]
		self.tagger = nltk.UnigramTagger(train_data)

# testing UnigramChunker's using the CoNLL-2000 Chunking Corpus resulting performance
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)

# using unigram tagger to assign a tag to each of the part-of-speech tags that appear in the corpus
postags = sorted(set(pos for sent in train_sents
		     for (word,pos) in sent.leaves()))
print unigram_chunker.tagger.tag(postags)

# establishing a baseline for the trivial chunk parser cp that creates no chunks
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)

# trying a naive regular expression chunker that looks for tags beginning with letters that are characteristic of noun phrase tags
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)

