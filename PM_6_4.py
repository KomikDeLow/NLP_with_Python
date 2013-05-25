import nltk
# define a feature extractor that builds a dictionary containing relevant information about a given name Marichka
def gender_features(word):
	return{'last_letter':word[-1]}
gender_features('Marichka')
{'last_letter': 'a'}
# prepare a list of examples and corresponding class labels
from nltk.corpus import names
import random
names=([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
# use the feature extractor to process the names data, and divide the resulting list of feature sets into a training set and a test set
featuresets=[(gender_features (p), m) for (p,m) in names]
train_set, test_set=featuresets[200:], featuresets[:200]
classifier=nltk.NaiveBayesClassifier.train(train_set)
# examine the classifier to determine which features it found most effective for distinguishing the names’ genders 
classifier.show_most_informative_features(30)
