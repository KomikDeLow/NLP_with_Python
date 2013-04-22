#IrynaShtanhret, AL-13, Chapter 7, Task 6
#Write one or more tag patterns to handle coordinated noun phrases, e.g., July/
#NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
#company/NN courts/NNS and/CC adjudicators/NNS.
import nltk
sentence=[("July","NNP"),("and","CC"),("August","NNP"),("all","DT"),("your","PRP$"),("managers","NNS"),("and","CC"),("supervisors","NNS"),("company","NN"),("courts","NNS"),("and","CC"),("adjudicators","NNS")]
grammar = "NP: {<DT>?<CC>?<PRP\$>?<NN.*>+}"#here I built a grammar
drawtree= nltk.RegexpParser(grammar)
result = drawtree.parse(sentence)
print result
result.draw()
