# Komar Mariia Als-11
# Chapter_5, Ex_31 

#Modify the program in Example 5-4 to use a logarithmic scale on the x-axis, by
#replacing pylab.plot() with pylab.semilogx(). What do you notice about the
#shape of the resulting plot? Does the gradient tell you anything?

# The shape of the resulting plot became straight.
# The gradient shows that the line can achieve 1.0 Perfomance 

import nltk
from nltk.corpus import brown
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.semilogx(sizes, perfs, '-bo')# replaced pylab.plot() with pylab.semilogx()
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

    
display()


