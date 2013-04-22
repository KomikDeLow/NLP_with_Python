# -*- coding: cp1251 -*-
#Iryna Shtanhret, AL-13, Task4, Chapter 7
#Початкове визначення  chunk (блок даних) - матеріал, який знаходиться між прогалинами.
#Створіть Chunker, що починається  з речення в одному блоці(chunk), решту роботи завершіть виключно шляхом заповнення прогалин.
#Визначте, які теги (або послідовність тегів), найімовірніше заповнять прогалини  за допомогою вашої власної ефективної програми.
#Порівняти продуктивність і доступність такого підходу порівняно з програмою-фрагментатором повністю базованою на правилах блоків(chunk).
import nltk
def chunked_tags(train):
   """Generate a list of tags that tend to appear inside chunks"""
    cfdist = nltk.ConditionalFreqDist()
    for t in train:
        for word, tag, chtag in nltk.chunk.tree2conlltags(t):
            if chtag == "O":
                cfdist[tag].inc(True)
            else:
                cfdist[tag].inc(False)
    return [tag for tag in cfdist.conditions() if cfdist[tag].max() == True]
train_sents = nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP'))
print chunked_tags(train_sents)
