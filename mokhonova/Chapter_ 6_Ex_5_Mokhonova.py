#Chapter_6_Ex_5_Mokhonova
 import nltk #importuju dani
 from nltk.corpus import names
 import random
 import math
 names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
 random.shuffle(names)# sortuju imena
 def gender_features(word):#funkciya vuznachennya rodu imen
	return {'last_letter': word[-1]}
print(gender_features('Peter-Nansy'))

featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)# produktyvnist' klasyfikatora Bayera
def entropy(labels):# vuznachennya rodu imen za dopomogoju entropiji
    freqdist = nltk.FreqDist(labels)
     probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
      return -sum([p * math.log(p,2) for p in probs])
    productivity=entropy(['male', 'female', 'male', 'male'])# produktyvnist' entropiji
   
