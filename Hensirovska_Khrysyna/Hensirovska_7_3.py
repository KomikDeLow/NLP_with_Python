# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#Розділ 7,завдання 3
#Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus. Inspect
#the data and try to observe any patterns in the POS tag sequences that make up
#this kind of chunk. Develop a simple chunker using the regular expression
#chunker nltk.RegexpParser. Discuss any tag sequences that are difficult
#to chunk reliably.
#import nltk
#Встановлюємо граматичне правило,яке визначає як речення мають бути поділені
#згідно chunking
#sentence=[("A","DT"),("dark","JJ"),("red","JJ"),("car","NN"),("came","VBD"),
          #("to","IN"),("a","DT"),("stopt","NN"),("in","IN"),("front","NN"),
          #("of","IN"),("the","DT"),("Flynn-Fletcher","JJ"),("residence","NN"),
          #("that","WDT"),("same","JJ"),("evening","NN"),(",",","),("in","IN"),
          #("another","DT"),("demension","NN"),(".",".")]
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#Створюємо синтаксичний аналізатор chunk.Це готовий клас,який створює екземи,
#виділяє іменникові вирази
#cp= nltk.RegexpParser(grammar)
#Реалізуємо синтаксичний аналізатор в реченнях
#result = cp.parse(sentence)
#print result
#result.draw()
#Використовуючи регулярні вирази, я побудувала наступний шаблон: {<DT>?<JJ>*<NN>}.
#Це правило працює тоді, коли chunker знайде визначник, після якого іде
#необмежена кількість прикметників, а в кінці стоїть іменник.
