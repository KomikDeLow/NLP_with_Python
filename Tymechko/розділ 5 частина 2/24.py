import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='news')
brown_sents=brown.sents(categories='news')
patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
        (r'.*', 'NN') # nouns (default)
        ]
regexp_tagger=nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print('Точність аналізатора')
print(regexp_tagger.evaluate(brown_tagged_sents))
patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	(r'.*ed$', 'VBD'), # simple past
        (r'(The|the|A|a|An|an|)$', 'AT'), #articles
	(r'.*es$', 'VBZ'), # 3rd singular present
        (r'.*able$', 'JJ'), # adjective -able
        (r'.*ful$', 'JJ'), # adjective -ful
        (r'.*ic$', 'JJ'), # adjective -ic
        (r'.*ive$', 'JJ'), # adjective -ive
        (r'.*less$', 'JJ'), # adjective -less
        (r'.*ous$', 'JJ'), # adjective -ous
        (r'.*ment$', 'NN'), # adjective -ment
        (r'.*ship$', 'NN'), # adjective -ship
        (r'.*dom$', 'NN'), # adjective -dom
        (r'.*tion$', 'NN'), # adjective -tion
        (r'.*ist$', 'NN'), # adjective -ist
        (r'.*ly$', 'RB'), # adjective -ly
        (r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
        (r'.*', 'NN') # nouns (default)
        ]
regexp_tagger=nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print('Точність аналізатора')
print(regexp_tagger.evaluate(brown_tagged_sents))
#Точність аналізатора, який був поданий у підручнику, складає 20%.
#Після того, як додали в аналізатор свої шаблони, його ефективність зросла до 30%.
#Функція evaluate допомагає нам дізнатись точність аналізатора
#при розробці і поступово відстежувати, як той чи інший шаблон покращує
#продуктивність аналізатора. 
#При розробці завдання, метод accurate() не вдалося використати.  Вибивало помилку. 
#Довелося використовувати функцію evaluate.
