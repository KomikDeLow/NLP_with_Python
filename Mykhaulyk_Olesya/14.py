#TODO
#Program is not well
#You use a lot variables (words_brown,tage_brown,tage_brown,sortyem,bez_dyblikativ) and it is a bad programming style
#You append tags to not empty tage_brown list
#Olesya Mykhaulyk ALs-12 5.10-14
#TODO
#What does your loop do?
import nltk
from nltk.corpus import brown
words_brown=brown.tagged_words()
tage_brown=[t for w,t in words_brown]
for i,j in words_brown:
        tage_brown.append(j)

	
set(sorted(tage_brown))

