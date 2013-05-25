

import nltk
fs1=nltk.FeatStruct("[C =?x,A = [B = ?x]]")
fs2=nltk.FeatStruct("[D =?x,C =?x,A = [B = ?x]]")
# визначаємо чи належить структура характеристик fs1 структурі fs2
print fs1.subsumes (fs2)
# визначаємо чи належить структура характеристик fs2 структурі fs1
print fs2.subsumes (fs1)
# функція, яка обєднує інформацію двох структур характеристик
# у випадку коли fs1 належить fs2
def subs (fs1, fs2):   
    if fs1.subsumes (fs2):
        print fs1.unify(fs2)
    elif fs2.subsumes (fs1):
        print fs2.unify(fs1)
    else: print "None"
print subs(fs1,fs2)
