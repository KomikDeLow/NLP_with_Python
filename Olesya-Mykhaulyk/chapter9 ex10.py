#Olesya Mykhaulyk
#ALs-12
#chapter 9 Ex.10
import nltk
#I create an informal algorithm  in order to unify featurestructures 
fs1 = nltk.FeatStruct ( Country = 'Ukraine', City = 'Lviv',PostCode='79031', Firma = 'Autolux')
fs2 = nltk.FeatStruct ( director = ' N.Petrovich ', activity = 'transportation' , Address = 'I.Boguna 5A', TelNumber='234 56 78')
print fs1.unify (fs2)# result's updatind and viewing 
