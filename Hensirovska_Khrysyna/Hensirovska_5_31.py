# TODO
# I need Python modul.
#

#Khrystyna Hensirovska,ALs-12
#Modify the program in Example 5-4 to use a logarithmic scale on the x-axis, by
#replacing pylab.plot() with pylab.semilogx(). What do you notice about the
#shape of the resulting plot? Does the gradient tell you anything?
import nltk
from nltk.corpus import brown
#використовуємо модель "Lookup Tagger"
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt,
    backoff=nltk.DefaultTagger('NN'))
#визначаємо один тег як параметр для інших,lookup tagger буде тільки зберігати
#пари слів-тегів,які не належать до частини мови іменник і якщо не можна
#визначити якою частиною мови є словотоді до нього застосовуватиметься
#default tagger
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
def display():
   import pylab
words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
sizes = 2 ** pylab.arange(15)
perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
#оцінюємо точність роботи аналізатора в залежності від кількості найчастотніших
#слів
pylab.semilogx(sizes, perfs, '-bo')# replaced pylab.plot()
#за умовою задачі замінюємо функцію pylab.plot() на pylab.semilogx()
pylab.title('Lookup Tagger Performance with Varying Model Size')
pylab.xlabel('Model Size')
pylab.ylabel('Performance')
pylab.show()
display()
plot()
#Дивлячись на графік,який ми отримали під час виконання програми можна зробити
#висновок,що функція plot будує графік елементів одновимірного масиву залежно
#від номера елемента,а функція semilogx використовує логарифмічний масштаб по
#осі х та лінійний по осі у.Тому один і той самий графік відображається по-іншому
#в залежності від того,яку функцію до нього застосовують.

