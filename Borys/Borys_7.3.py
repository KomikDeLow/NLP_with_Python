import nltk
from nltk.corpus import conll2000
grammar="NP: {<DT|JJ>?<RB>?<VBN>?<NN.*>+}" # Creating grammar rule
sent='Forecsasts for the trade figures range widely but few economists expect the data to show a very marked improwment from the 2 billion deficit in the current account reported for August'
sentence=sent.split()
tagged=nltk.pos_tag(sentence)
cp=nltk.RegexpParser(grammar) # Grammar based parser
result=cp.parse(tagged) # parsing sentence
print result


