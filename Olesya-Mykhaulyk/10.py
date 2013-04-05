# TODO
# I didn't understand "rozbuvaemo na tegu"? zadaemo parametr? nakladaem na novui tekst z rozdily news? 
#Olesya Mykhaulyk ALs-12 5/10-10
import nltk
from nltk.corpus import brown # importyemo korpus brown
brown_sents=brown.sents(categories='humor')# vuburaem kategoriy humor
brown_tagged_sents=brown.tagged_sents(categories='humor')#rozbuvaemo tekst danoi kategorii na tegu
unigram_tagger=nltk.UnigramTagger(brown_tagged_sents)#zadaemo parametr dla trenyvanja
unigram_tagger.tag(brown_sents[50])
brown_tagged_sents_1=brown.tagged_sents(categories='news')#zapyskaem analizator na teksti kategorii news
brown_sents_1=brown.sents(categories='news')
unigram_tagger.tag(brown_sents_1[50])# zna4enna NONE prusvoyetsa vsim slovam, jaki ne zystri4aytsa v tekstah na osnovi jakuh provoduvsa analiz(tobto tsi slova vidsytni y spusky nai4astotniwuh)
