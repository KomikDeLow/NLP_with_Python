import nltk
chunk_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(chtree)]
              for chtree in nltk.corpus.conll2000.chunked_sents('train.txt')]
unigram_chunker = nltk.UnigramTagger(chunk_data)
print unigram_chunker.evaluate(chunk_data)
bigram_chunker = nltk.BigramTagger(chunk_data, backoff=unigram_chunker)
print bigram_chunker.evaluate(chunk_data)
trigram_chunker = nltk.TrigramTagger(chunk_data, backoff=bigram_chunker)
print trigram_chunker.evaluate(chunk_data)

