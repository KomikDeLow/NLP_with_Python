# Irena Marunyshyn PRLs-12
#Ignoring structure sharing, give an informal algorithm for unifying two feature
#structures.
import nltk
fs1 = nltk.FeatStruct ( Country = 'USA', City = 'Chicago', Firma = 'American Life') # creating an informal algorithm for unifying two featurestructures
fs2 = nltk.FeatStruct ( director = ' B. Birtsch ', product = 'computers' , Address = ' Washynhton street')
print fs1.unify (fs2)# update and print result with my two stuctures
