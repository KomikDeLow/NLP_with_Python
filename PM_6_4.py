import nltk
def gender_features(word):
	return{'last_letter':word[-1]}
gender_features('Marichka')
{'last_letter': 'a'}
from nltk.corpus import names
import random
names=([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
featuresets=[(gender_features (p), m) for (p,m) in names]
train_set, test_set=featuresets[200:], featuresets[:200]
classifier=nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(30)
