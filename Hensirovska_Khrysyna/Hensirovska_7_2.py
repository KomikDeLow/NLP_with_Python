#Генсіровська Христина,ПРЛс-12
#Розділ 7,завдання 2
#Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
#to do this by generalizing the tag pattern that handled singular noun phrases.
#import nltk
#sentence = [("many", "JJ"), ("researches", "NNS"),(",", ","), ("two", "CD"),
           # ("weeks", "NNS"),(",", ","), ("both", "DT"), ("new", "JJ"),
           # ("positions", "NNS")]
#Встановлюємо граматичне правило,яке визначає як речення мають бути поділені
#згідно chunking
#grammar = "NP: {<DT|CD>?<JJ>*<NN.>}"
#Створюємо синтаксичний аналізатор chunk.Це готовий клас,який створює екземи,
#виділяє іменникові вирази
#cp = nltk.RegexpParser(grammar)
#Реалізуємо синтаксичний аналізатор в реченнях
#result = cp.parse(sentence)
#print result
#result.draw()
#На малюнку зображені іменникові вирази, що включають в себе іменники множини.
