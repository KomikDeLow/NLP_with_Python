#Khrystyna Hensirovska,ALs-12
#Chapter 9,task 3
#Write a function subsumes() that holds of two feature structures fs1 and fs2 just
#in case fs1 subsumes fs2.
import nltk
#Ми використовуємо ф-кцію FeatStruct  для визначення особливих структур в NLTK
#Ці особливості можуть набувати значення  string або integer.Особлива структура
#є тільки видом словника,отже,ми доступаємось до його значення простим
#індексуванням.Ми можемо використовувати наш звичайний синтаксис,щоб визначити
#значення для особливостей.
fs1=nltk.FeatStruct("[C =?x,A = [B = ?x]]")
#Визначаємо особливості структури,яка має складне значення
fs2=nltk.FeatStruct("[D =?x,C =?x,A = [B = ?x]]")
print fs1.subsumes (fs2) #перевірямо чи fs1 включена в fs2
print fs2.subsumes (fs1)#перевірямо чи fs2 включена в fs1
#За допомогою цієїф-кції ми об"єднуємо дві особливі структури fs1 та fs2,в тому
#випадку,якщо fs1 включена в fs2
def subs (fs1, fs2):
	if fs1.subsumes (fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes (fs1):
		print fs2.unify(fs1)
	else: print "None"
	print subs(fs1,fs2)
