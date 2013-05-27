# fine
# Fuyarchuk O/ Chapter 9 Task 3
import nltk
fs1=nltk.FeatStruct("[C =?x,A = [B = ?x]]")
fs2=nltk.FeatStruct("[D =?x,C =?x,A = [B = ?x]]")
print fs1.subsumes (fs2)# Визначаємо чи належить структура характеристик fs1 структурі fs2
print fs2.subsumes (fs1)# Визначаємо чи належить структура характеристик fs2 структурі fs1
def subs (fs1, fs2): # функція, яка обєднує інформацію двох структур характеристик
                    #у випадку коли fs1 належить fs2
    if fs1.subsumes (fs2):
        print fs1.unify(fs2)
    elif fs2.subsumes (fs1):
        print fs2.unify(fs1)
    else: print "None"
print subs(fs1,fs2)
