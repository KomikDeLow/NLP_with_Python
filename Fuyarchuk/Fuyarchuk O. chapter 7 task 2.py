# Фуярчук О. Розділ 7 Задача 2
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" # Define a chunk grammar
bk=nltk.RegexpParser(grammar)# Using this grammar we create a chunk parser
result=bk.parse(sentence)#Test this chunk on our example
print result
print bk.evaluate(result)

