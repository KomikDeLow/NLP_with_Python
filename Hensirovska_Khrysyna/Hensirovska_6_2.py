# Khrystyna Hensirovska
#ALs-12
#Chapter 6
#Task 2
#Using any of the three classifiers described in this chapter, and any features you
#can think of, build the best name gender classifier you can. Begin by splitting the
#Names Corpus into three subsets: 500 words for the test set, 500 words for the
#dev-test set, and the remaining 6,900 words for the training set. Then, starting with
#the example name gender classifier, make incremental improvements. Use the devtest
#set to check your progress. Once you are satisfied with your classifier, check
#its final performance on the test set. How does the performance on the test set
#compare to the performance on the dev-test set? Is this what you’d expect?
#import nltk
#from nltk.corpus import names
#import random
#Визначаємо характерний екстрактор,підготовляємо список прикладів та відповідних
#класових позначок
#names = ([(name, 'male') for name in names.words('male.txt')] +
	# [(name, 'female') for name in names.words('female.txt')])
	#random.shuffle(names)
#характерний екстрактор,який описує гендерні особливості для відносто малого
#корпусу імен
	#def gender_features(name):
	#features={}
	#features['firstletter']=name[0].lower() 
	#features['lastletter']=name[-1:].lower() 
	#for letter in 'abcdefghijklmnopqrstuvwxyz':
		#features["count(%s)" % letter] = name.lower().count(letter)
		#features["has(%s)" % letter] = (letter in name.lower())
		#return features
	
#random.shuffle(names)
#Використовуємо продуктивний метод-error anaalysis.Спочатку,ми обираємо
#development set,що включає дані корпусу для створення моделі.
#Development set потім поділяється на training set та dev-test set
	#featuresets = [(gender_features(n), g) for (n,g) in names]
	#test_set=featuresets[:500] використовується для оцінки системи
	#dev_test_set=featuresets[500:1000] використовується для виконання
#аналізу над помилками

	#train_set=featuresets[1000:] використовується для тренування моделі
	#classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print nltk.classify.accuracy(classifier, dev_test_set)\ Визначає
#точність послідовного класифікатора аналізу над помилками
	#print nltk.classify.accuracy(classifier, test_set) Визначає точність
#послідовного класифікатора оцінки системи
#В нашому завданні точність послідовного класифікатора аналізу над помилками склала 74%,
#а точність послідовного класифікатора оцінки сиcтеми склала 76%
	
