#Olesya Mykhaulyk
#ALs-12
#Chapter 5 Ex.31
def performance (cfd, wordlist):
    lt=dict((word, cfd[word].max()) for word in wordlist
    baseline_tagger=nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
 def display():
   import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news'))) 
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news')) 
    sizes = 2 ** pylab.arange(15) 
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes] 
    pylab.semilogx(sizes, perfs, '-bo') 
    pylab.title('Lookup Tagger Performance with Varying Model Size') 
    pylab.xlabel('Model Size') 
    pylab.ylabel('Performance') 
    pylab.show() 

display()
#plot() function builts a one-dimensional array according to the element's number
#the same scale while using different functions is presented in different ways
#because semilog x() function uses the logarithmic scale on the x-axis and
#the lineal scale on the y-axis