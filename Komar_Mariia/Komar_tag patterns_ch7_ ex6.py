#Komar Mariia ALs-11 Chapter_7 Ex_6
#Write one or more tag patterns to handle coordinated noun phrases

import nltk
sentence = [ ("July", "NNP"), ("and", "CC"), ("August", "NNP"),("all", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and","CC"),("supervisors","NNS"),("company","NN"),("courts","NNS"),("and","CC"),("adjudicators","NNS")]#create sentence
grammar = "NP:{<DT>?<PRP$>?<NN.*>+<CC><NN.*>*}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result

