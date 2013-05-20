# TODO
# What does your program do?
# it rebuilds trigram chunker in order to enhance accuracy

import nltk
chunk_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(chtree)] 
for chtree in nltk.corpus.conll2000.chunked_sents('train.txt')] #building a new unigram chunker,using training sentences in a chunking cirpus
unigram_chunker = nltk.UnigramTagger(chunk_data)
print unigram_chunker.evaluate(chunk_data)
bigram_chunker = nltk.BigramTagger(chunk_data, backoff=unigram_chunker) #building a bigram chunker
print bigram_chunker.evaluate(chunk_data)
trigram_chunker = nltk.TrigramTagger(chunk_data, backoff=bigram_chunker) #building a trigram chuncker
print trigram_chunker.evaluate(chunk_data)  
# having seen, that bigram chunker scores almost 90% accuracy, we have rebuilt a trigram chunker, but it has a slightly lower perfomance.
