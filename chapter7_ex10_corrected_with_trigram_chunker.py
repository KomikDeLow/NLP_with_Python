#Presented by Iuliia Tsymbalista ALs-13
# chapter 7, ex.10
#The bigram chunker scores about 90% accuracy. Study its errors and try to work
#out why it doesn’t get 100% accuracy. Experiment with trigram chunking. Are you
#able to improve the performance any more?



# creating trigram chunker
import nltk
chunk_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(chtree)]
  for chtree in nltk.corpus.conll2000.chunked_sents('train.txt')]
tokens=[t for t,c in chunk_data[0]]
trigram_chunker=nltk.TrigramTagger(chunk_data)
list(trigram_chunker.tag(tokens))
print trigram_chunker.evaluate(chunk_data)

# for higher accuracy I create unigram and bigram chunkers and use them with the trigram chunker
unigram_chunker = nltk.UnigramTagger(chunk_data)
bigram_chunker = nltk.BigramTagger(chunk_data, backoff=unigram_chunker)
trigram_chunker=nltk.TrigramTagger(chunk_data, backoff=bigram_chunker)
print trigram_chunker.evaluate(chunk_data)
