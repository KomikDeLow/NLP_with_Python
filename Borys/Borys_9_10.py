# Roman Borys PRLs-11
import nltk
#encoding restaurant information
fs1=nltk.FeatStruct(CITY='Lviv',STREET='V. Velykogo',RESTAURANT='NY Street Pizza')
#exploring feature structure
fs2=nltk.FeatStruct(FEEDBACK='Good',TABLES='10')
print fs2.unify(fs1) #Merging information from two feature structures
