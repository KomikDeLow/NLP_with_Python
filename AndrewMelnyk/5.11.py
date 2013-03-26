# TODO
# I didn't see your program result

#Andrew Melnyk ALs-12 27.02.12
import nltk
from nltk.corpus import brown
training=brown.tagged_sents(categories='news') #Змінна яка запам'ятовує використання тегів у вже промаркованому тексті
sent=('Stephane Hessel the former French Resistance fighter whose 2010 manifesto Time for Outrage inspired social protesters in Europe dies aged 95').split() #Обрав довільне речення з яким я працюватиму
#Використання AffixTagger з різними значеннями affix_length та min_stem_length
for i in range(4):
	affix_tagger=nltk.AffixTagger(training,affix_length=int(i),min_stem_length=int(i))
	affix_tagger.tag(sent)
	affix_tagger.evaluate(brown.tagged_sents(categories='news'))
