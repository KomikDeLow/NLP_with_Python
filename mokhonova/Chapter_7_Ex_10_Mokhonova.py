# Chapter_7_Ex_10_Mokhonova
import nltk
chunk_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(chtree)]
  for chtree in nltk.corpus.conll2000.chunked_sents('train.txt')]
tokens=[t for t,c in chunk_data[0]]
trigram_chunker=nltk.TrigramTagger(chunk_data)
list(trigram_chunker.tag(tokens))
print trigram_chunker.evaluate(chunk_data)
# stvorjuju unigram i bigram chunkers i vykorystovuju jih z poperedim chunker
unigram_chunker = nltk.UnigramTagger(chunk_data)
bigram_chunker = nltk.BigramTagger(chunk_data, backoff=unigram_chunker)
trigram_chunker=nltk.TrigramTagger(chunk_data, backoff=bigram_chunker)
print trigram_chunker.evaluate(chunk_data)
