# TODO
# I need Python modul.
#

#Генсіровська Христина,ПРЛс-12
#розділ 6,завдання 8
#Особливості слова дуже корисні для здійснення документного класифікатора,
#адже слова, які з’являються в документі, вказують на семантичний контекст
#цього слова. Проте, велика кількість слів з’являється дуже рідко і більшість
#інформативних слів можуть взагалі не з’явитися під час нашого програмування. 
#Щоб не допустити цього, можна використати словниковий запас, який буде
#демонструвати, як різні слова пов’язані між собою. Використовуючи словник
#WordNet, доповніть the movie review document класифікатор, щоб можна було
#узагальнити слова, які з’являються в документі. Це повинно призвести до того,
#що ці слова будуть співпадати з словами із тренувальних даних.
import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
#Використовуємо корпус Movie Reviews Corpus,який класифікує кожен розгляд
#як позитивний чи негативний
#Визначаємо feature extractor для документів,щоб класифікатор знав на які
#аспекти даних потрібно звернути увагу
documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)[:100]]
random.shuffle(documents)
#Обмежуємо число слів,які має опрацювати класифікатор,розпочинаємо створенням
#списку,який складається з 2 тисяч найбільш вживаних слів у всьому корпусі
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_words)
word_features = all_words.keys()[:200]
#Перевіряємо чи кожне з цих слів присутнє у даному документі
#Обчмслюємо число всіх слів у документі
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
		return features
        #Тренуємо і тестуємо класифікатор за допомогою документної класифікації
	featuresets = [(document_features(d), c) for (d,c) in documents]
	train_set, test_set = featuresets[80:], featuresets[:20]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)
	for word in all_words.keys()[:300]:
		if all_words[word]< all_words[all_words.keys()[200]]:
			for synset in wn.synsets(word):
				for hypernyms in synset.hypernyms():
					for l_names in hypernyms.lemma_names:
						if l_names in all_words.keys()[:200]:
							if word not in word_features:
								word_features.append(word)
								print len(word_features)
								featuresets = [(document_features(d), c) for (d,c) in documents]
								train_set, test_set = featuresets[80:], featuresets[:20]
								classifier = nltk.NaiveBayesClassifier.train(train_set)
       #Щоб перевірити наскільки достовірними є результати класифікатора ми
       #обчислюємо його точність за допомогою test set	
								print nltk.classify.accuracy(classifier, test_set)

#Як бачимо, базова точність аналізатора складає 63%. Після того, як я добавила
#слова, які не входять в список найчастотніших, проте їхні гіперніми входять,
#то точність аналізатора зросла до 66%. Кількість таких слів склала 38.
