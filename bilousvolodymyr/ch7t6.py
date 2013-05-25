#Bilous Volodymyr,AL-11
#chapter 7, task 6
import nltk
sentence=[("July","NNP"),("and","CC"),("August","NNP"),("all","DT"),("your","PRP$"),("managers","NNS"),("and","CC"),("supervisors","NNS"),("company","NN"),("courts","NNS"),("and","CC"),("adjudicators","NNS")]
grammar = "NP: {<DT>?<CC>?<PRP\$>?<NN.*>+}"# Building the grammar
print grammar
drawtree= nltk.RegexpParser(grammar)
result = drawtree.parse(sentence)
print result
result.draw()
# NP ommit DT and PRP$ in resulted NP, however they are included in grammar'
