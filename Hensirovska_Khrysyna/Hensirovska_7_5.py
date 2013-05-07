# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#Розділ 7,завдання 5
#Write a tag pattern to cover noun phrases that contain gerunds, e.g., the/DT
#receiving/VBG end/NN, assistant/NN managing/VBG editor/NN. Add these patterns
#to the grammar, one per line. Test your work using some tagged sentences of
#your own devising.
#import nltk
#Встановлюємо граматичне правило,яке визначає як речення мають бути поділені
#згідно chunking
#grammar = r"""
#Шукаємо варіанти,що можна віднести до іменникового виразу.
#Регулярний вираз потрібно сформувати коли chunker знайде на першому місці
#optional determiner(DT) або іменник ,потім дієслово(може бути,або не
#бути в регулярному виразі) з іменником
#NP:{<DT|NN>?<VBG><NN>}"""
#define an example sentence to be chunked
#sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","),
           # ("assistant","NN"),("managing","VBG"),("editor","NN")]
#Створюємо синтаксичний аналізатор chunk.Це готовий клас,який створює
#екземи,виділяє іменникові вирази
#cp = nltk.RegexpParser(grammar)
#run the chunker on this input
#print cp.parse(sentence)
#sentence= [("A","DT"),("dark","JJ"),("red","JJ"),("car","NN"),
          # ("came","VBD"),("to","IN"),("a","DT"),("stopt","NN"),("in","IN"),
           #("front","NN"),("of","IN"),("the","DT"),("Flynn-Fletcher","JJ"),
           #("residence","NN"),("that","WDT"),("same","JJ"),("evening","NN"),
           #(",",","),("in","IN"),("another","DT"),("demension","NN"),(".",".")]
#Створюємо синтаксичний аналізатор chunk.Це готовий клас,який створює екземи,
#здійснює виділення іменникових виразів
#cp= nltk.RegexpParser(grammar)
#run the chunker on this input
#print cp.parse(sentence)
