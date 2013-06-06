# Chapter_7_Ex_2_Fursachyk
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" # opusyjemo gramatyku
bk=nltk.RegexpParser(grammar)# Vykorystovujuchy cju gramatyku my stvorjujemo syntaksychnyj̆ analizator
result=bk.parse(sentence)#Testujemo jogo na nashomu prykladi
print result
from nltk.corpus import conll2000 # importujemo korpus conll2000
cp = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # vyvodymo rezul'tat
