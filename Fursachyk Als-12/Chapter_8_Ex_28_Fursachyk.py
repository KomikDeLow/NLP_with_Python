#Chapter_8_Ex_28_Fursachyk
import nltk
from nltk.corpus import treebank
l = treebank.parsed_sents()[:10]# список 10 синтаксично проаналізованих дерев
allproductions = []# список правил
for tree in l:
    for p in tree.productions():
        allproductions.append(p)# додавання правил у список


from nltk import FreqDist
fd=FreqDist(allproductions)
print fd.hapaxes()# виведення правил, які використовуються тільки один раз
