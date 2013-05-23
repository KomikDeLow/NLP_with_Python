

import nltk
from nltk.corpus import senseval
instances = senseval.instances('serve.pos')
features=[] # open corpus data
for inst in instances:
    context = [c if isinstance(c, tuple) else (c, "None") for c in inst.context]
    # converting strings in "contex" to (string, "None") tuples in order to create a dictionary
    f = dict(context)
    # creating a dictionary
    f.update({"word": inst.word, "position": inst.position})
    # updating features "word" and "position"
    features.append((f, ' '.join(inst.senses)))

size = int(len(features) * 0.1) # set an amount of testing data (10%)
train_set, test_set = features[size:], features[:size] # making two data sets (for training and testing)
classifier1 = nltk.NaiveBayesClassifier.train(train_set) # training the classifier
print nltk.classify.accuracy(classifier1, test_set) # evaluating the accuracy of the classifier
