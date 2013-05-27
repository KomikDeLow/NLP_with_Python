# fine
#Komar Mariia, ALs-11
#Chapter_9, Ex_10

#Ignoring structure sharing, give an informal algorithm for unifying two feature
#structures.

import nltk
fs1=nltk.FeatStruct(COUNTRY='UKRAINE', CITY='LVIV', UNIVERSITY='LVIV POLYTECHNIK') #створюємо першу структуру ознак
fs2=nltk.FeatStruct(ACADEMIC_INSTITUTES='ICSIT', DEPARTMENT='APLIED LINGUISTC')#створюємо другу структуру ознак
print fs1.unify(fs2) #здійснюємо операцію уніфікації
