# error
#Khrystyna Hensirovska,ALs-12
#Chapter 9,task 10
#Ignoring structure sharing, give an informal algorithm for unifying two feature
#structures.
mport nltk
#encode information about a hotel in a feature structure
fs1=nltk.FeatStruct(CITY='Ivano-Frankivsk',STREET='Ivana Franka',HOTEL='Nadia')
#exploring feature structure
fs2=nltk.FeatStruct(stars='three',rooms='one hundred')
print fs2.unify(fs1) #Merging information from two feature structures is called unification and is supported
#by the unify() method.
