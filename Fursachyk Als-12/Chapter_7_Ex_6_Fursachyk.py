#Chapter_7_Ex_6_Fursachyk
import nltk
phrases=[("July", "NNP"), ("and", "CC"), ("August", "NNP"),(",",","), ("all", "DT"), ("your", "PRP$"), 
   	  ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"),(",",","), ("company", "NN"), 
   	  ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")]
grammar="NP:{<NN.>?<DT>?<PRP$>?<NNS>?<CC><NN.>}" # opysuju gramatyku
cp=nltk.RegexpParser(grammar) # vykorystovujuchy gramatyku my stvorjujemo chunk parser
results=cp.parse(phrases)
print results
