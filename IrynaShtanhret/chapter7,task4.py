#Iryna Shtanhret, AL-13, Task4, Chapter 7
#Початкове визначення  chunk (блок даних) - матеріал, який знаходиться між прогалинами.
#Створіть Chunker, що починається  з речення в одному блоці(chunk), решту роботи завершіть виключно шляхом заповнення прогалин.
#Визначте, які теги (або послідовність тегів), найімовірніше заповнять прогалини  за допомогою вашої власної ефективної програми.
#Порівняти продуктивність і доступність такого підходу порівняно з програмою-фрагментатором повністю базованою на правилах блоків(chunk).

import nltk
#some sentence
sentence = [("Apple", "NNP"), ("is", "VBZ"), ("the", "DT"),
            ("leader", "NN"), ("in", "IN"), ("computer", "JJ"),
            ("technology", "NN")] 
#define grammar, at first chunk everything and then chink
grammar = r"""
NP:
	{<.*>+}
	}<VBD|IN|CC|IN|MD|RB|RBR|RP|SYM|TO|UH|VB|VBD|VBG|VBN|VBP|VBZ|WRB>+{
	"""
cp = nltk.RegexpParser(grammar)  #create a chunk parser
result = cp.parse(sentence)    #present result
print result
