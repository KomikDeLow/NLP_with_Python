# TODO
# test your parser on real sentences that consist NP with JJ NN, JJ NNS....
# accuracy of your parser?

# Фуярчук О. Розділ 7 Задача 2

import nltk
sentence=[("much","JJ"),("sugar","NN"),("agile","JJ"),("boys","NNS"),
          ("three","CD"),("flowers","NNS"),("beautiful","JJ"),("garden","NN")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" # Define a chunk grammar
bk=nltk.RegexpParser(grammar)# Using this grammar we create a chunk parser
result=bk.parse(sentence)#Test this chunk on our example
print result

