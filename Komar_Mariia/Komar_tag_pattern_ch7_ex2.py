# Komar Mariia ALs-11, Chapter_7, Ex_2
# Write a tag pattern to match noun phrases containing plural head nouns.
# Do this by generalizing the tag pattern that handled singular noun phrases.


import nltk, re, pprint
sentence = [("many","JJ"), ("researchers","NNS"), ("two","CD"), ("weeks","NNS"), ("both","DT"), ("new","JJ"), ("positions","NNS")]#create sentence
grammar = "NP: {<DT>*<CD>*<JJ>*<NN.*>+}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result
