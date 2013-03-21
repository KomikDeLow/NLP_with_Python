#Olesya Mykhaulyk ALs-12 5.10-14
import nltk
from nltk.corpus import brown
words_brown=brown.tagged_words()
tage_brown=[t for w,t in words_brown] # vuburaem z korpysy tegu vsih sliv
for i,j in words_brown:
        tage_brown.append(j)

	
sortyem=sorted(tage_brown)
bez_dyblikativ=set(sortyem)
bez_dyblikativ
