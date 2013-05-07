# TODO
# unexpected indent!!!
#

# Vezdenko
 import nltk
 sentence = [ ("All", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and","CC"),
	       ("supervisors","NNS"), ("arrived", "VBD"), ("at","IN"),
	       ("July", "NNP"), ("and", "CC"), ("August", "NNP")]#створила реченн€
 grammar="NP:{<DT>?<PRS$>?<NN.*>+<CC><NN.*>*}"#створила регул€рний вираз
 cp=nltk.RegexpParser(grammar)#створила chunk parser у нашому приклад≥
 result=cp.parse(sentence)#test chunk parser у моЇму реченн≥
 print result#видруковуЇмо результат
