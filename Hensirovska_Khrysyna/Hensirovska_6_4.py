# TODO
# I need Python modul.
#

#import nltk
#from nltk.corpus import movie_reviews
#import random
#Ми визначаємо характерний екстрактор для документів,щоб класифікатор
#знав на які аспекти даних потрібно звернути увагу
#documents= [(list(movie_reviews.words(fileid)),category)
        # for category in movie_reviews.categories()
         #for fileid in movie_reviews.fileids(category)]
#random.shuffle(documents)
#Для того щоб обмежити число слів,які необхідно опрацювати класифікаторові,
#ми розпочинаємо створення списку з 2 тисяч найбільш вживаних слів в цілому
#корпусі.
#all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
#word_features=all_words.keys() [:2000]
#Визначаємо характерний екстрактор,який просто перевіряє чи кожне з цих
#слів присутнє у даному документі
#def document_features(document):
    #document_words= set(document)
    #features= {}
    #for word in word_features:
         #features['contains(%s)' % word] = (word in document_words)
   # return features
#Щоб перевірити наскільки достовірним є результуючий класифікатор,ми
#обчислюємо його точність за допомогою test_set
#featuresets= [(document_features(d), c) for (d,c) in documents]
#train_set, test_set = featuresets[:100], featuresets[:100]
#classifier= nltk.NaiveBayesClassifier.train(train_set)
#Шукаємо які класифікатори слів є найбільш інформативними
#classifier.show_most_informative_features(30)
#На мою думку ці слова є найбільш інформативними,тому що будь-яке з цих
#слів несе в собі конкретні значення і асоціації.Почувши одне з цих слів
#можна відразу сказати до яких слів воно належить (позитивних чи негативних)
#Найбілше,що мене здивувало серед цих результатів,це те,що поряд з прикмет-
#никами і прислівниками знаходяться імена акторів та назви видуманих героїв.
#Наприклад,Seagal (Стівен Сігал)зустрічається у 8 раз частіше у негативному
#значенні,ніж у позитивному,хоча,він зазвичай грає ролі "хороших хлопців".
#Damon(Мет Деймон),теж актор і він зустрічається в 6 разів частіше в пози-
#тивному значенні,ніж в негативному.Слово jedi (Джедай) зустрічається в 4
#рази частіше у позитивному значенні,ніж у негативному.
