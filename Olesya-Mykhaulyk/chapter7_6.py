#Olesya Mykhaulyk
#ALs-12
#Chapter 7 Ex 6 corrected
import nltk
phrases=[("July", "NNP"), ("and", "CC"), ("August", "NNP"),(",",","), ("all", "DT"), ("your", "PRP$"), 
   	  ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"),(",",","), ("company", "NN"), 
   	  ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")]
grammar="NP:{<NN.>?<DT>?<PRP$>?<NNS>?<CC><NN.>}" # set grammar
cp=nltk.RegexpParser(grammar) # using grammar we create chunk parser
results=cp.parse(phrases)
print results
