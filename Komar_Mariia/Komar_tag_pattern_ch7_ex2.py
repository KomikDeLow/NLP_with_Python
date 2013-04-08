# TODO
# Test your parsen on real sentences that contain NP with JJ NNS, CD NNS


# Komar Mariia ALs-11, Chapter_7, Ex_2
# Write a tag pattern to match noun phrases containing plural head nouns.
# Do this by generalizing the tag pattern that handled singular noun phrases.


import nltk, re, pprint
sentence = [("Many","JJ"), ("researchers","NNS"), ("developed","VBD "), ("both","DT"),
            ("new","JJ"), ("positions","NNS"), ("two","CD"), ("weeks","NNS"), ("ago","RB")]#create sentence
grammar = "NP: {<DT>*<CD>*<JJ>*<NN.*>+}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result
