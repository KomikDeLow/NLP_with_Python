# fine
# TODO
# Comments?
# I see this program in Shudlo branch today !!! (This task was done together with her, it just was submited in different time. I can redo this task if nessasery.)

# Building a classifier which should predict wich of these:(storong,powerfull) should be used
import nltk
import random
from nltk.corpus import brown
tagged_words=brown.tagged_words() # building a list of all words
bigram_list=nltk.bigrams(tagged_words)# bulding a bigram list of all words
bigram_needed=[w for w in bigram_list if w[0][0].lower() in ['strong','powerful']] # taking out bigrams that have "strong" and "powerfull" in them
def feature11((w,p)): # building a function which gets feature of a word (words + position)
	return {'word':p[0],'Pos':p[1]} # it returns a dictionary
featureSet=[]
for word in bigram_needed:
	featureSet.append((feature11(word),word[0][0])) # building a cycle to create a set of data with features for the classifier
test_data=featureSet[:120]
train_data=featureSet[120:]# dividing test and train data

classifier = nltk.NaiveBayesClassifier.train(train_data) # training the classifier

print 'Clasifier accuraci: ',100.0 * nltk.classify.accuracy(classifier, test_data),'%' # evaluating the builded classifier
