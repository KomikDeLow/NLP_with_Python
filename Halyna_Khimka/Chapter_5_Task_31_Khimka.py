#Halyna Khimka
#Chapter 5, Task 31
# Modify the program in Example 5-4 to use a logarithmic scale on the x-axis, by
#replacing pylab.plot() with pylab.semilogx(). What do you notice about the
#shape of the resulting plot? Does the gradient tell you anything?
#Funkcija plot() buduje grafik elementiv odnovymirnogo masyvu v zalezhnosti vid nomera elementa.
#Tobto do 16384-go elementa (sizes)
#Funlcia semilogx() vukorystovuje logaryfmi4nyj masshtab po osi x ta linihnyj po osi y.
#Tomy cej samyj grafik pry vykorystanni riznyh funkcij vidobrazhajetjsja po-riznomu.
#
#
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
        pylab.semilogx(sizes, perfs, '-bo')
        pylab.title('Lookup Tagger Performance with Varying Model Size')
        pylab.xlabel('Model Size')
        pylab.ylabel('Performance')
        pylab.show()

display()

        
