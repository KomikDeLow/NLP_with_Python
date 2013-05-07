import nltk
from nltk.corpus import brown
#using "Lookup Tagger" model
def performance(cfd, wordlist):
lt = dict((word, cfd[word].max()) for word in wordlist)
baseline_tagger = nltk.UnigramTagger(model=lt,
backoff=nltk.DefaultTagger('NN'))
default tagger
return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
def display():
import pylab
words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
sizes = 2 ** pylab.arange(15)
perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
#identifying analysis precision, depending how many common
#words are in use
pylab.semilogx(sizes, perfs, '-bo')# replaced pylab.plot()
# replacing  pylab.plot() with pylab.semilogx() 
with pylab.semilogx()
pylab.title('Lookup Tagger Performance with Varying Model Size')
pylab.xlabel('Model Size')
pylab.ylabel('Performance')
pylab.show()
display()

