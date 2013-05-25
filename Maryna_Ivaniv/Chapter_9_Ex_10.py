#Maryna Ivaniv PRLs-11 Chapter 9, Ex.10

#Ignoring structure sharing, give an informal algorithm for unifying two feature
#structures.

import nltk
fs1=nltk.FeatStruct(COUNTRY='ITALY', CITY='MILAN', THEATRE='LA SCALA')
fs2=nltk.FeatStruct(OPERA='MADAMA_BUTTERFLY', ACTRESS='SLOMIYA_KRUSHELNYTSKA')
print fs1.unify(fs2)
