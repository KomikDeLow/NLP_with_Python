# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#Розділ 8,завдання 14
#You can modify the grammar in the recursive descent parser demo by selecting
#Edit Grammar in the Edit menu. Change the first expansion production, namely
#NP -> Det N PP, to NP -> NP PP. Using the Step button, try to build a parse tree.
#What happens?
#import nltk
#sent = ['I', 'loved', 'rain'] створюємо речення
#Встановлюємо просту контекстно-вільну граматику для створеного речення
#grammar1 = nltk.parse_cfg("""
#S -> NP VP
#NP -> DET N PP
#NP -> "I"
#VP -> V NP
#V -> "loved"
#NP -> "rain"
#""")
#sent = "I loved rain".split()
#програма синтаксичного аналізу
#rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
#виводимо результати на екран
#result = rd_parser.parse(sent)
#виводимо графічні результати на екран
#result.draw()
#Згідно з умовою задачі додаємо правила до граматики.Замінюємо NP -> Det N PP,
#на NP -> NP PP
#grammar1 = nltk.parse_cfg("""
#S -> NP VP
#NP -> NP PP
#NP -> "I"
#VP -> V NP
#V -> "loved"
#NP -> "rain"
#""")
#sent = "I loved rain".split()
#програма синтаксичного аналізу
#rd_parser = nltk.RecursiveDescentParser(grammar1, trace = 3)
#виводимо результати на екран
#result = rd_parser.parse(sent)
#Після додавання правила до граматики відбувається зациклення.
