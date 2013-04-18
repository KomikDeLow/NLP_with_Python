# TODO
# and the remaining 6,900 words for the training set
#
# Andrew Melnyk ALs-12
 
import nltk
from nltk.corpus import names
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')]) 	# ����� � ��� �������� ���������� ��� ����� � ����

def gender_features(name): # ��������� ������� ��� ���� ���������� �������� ���������� ����
        features = {}
        features["lastletter"] = name[-1].lower()
        features["suffix1"] = name[-2:].lower()
        features["suffix2"] = name[-3:].lower()
        features["suffix3"] = name[-4:].lower()
        return features
# ����������� ������ ���� �� 3 ������� ����� ����� ��������
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set = featuresets[500:]
dev_test_set = featuresets[500:1000]
test_set = featuresets[1000:]
# ��������� ������������ NaiveBayes
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_test_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(20)
