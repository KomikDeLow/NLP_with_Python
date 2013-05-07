# TODO
# I don't see that your constraints working
#


# Komar Mariia Als-11
# Chapter_9, Ex_1

# What constraints are required to correctly parse word sequences like
# I am happy and she is happy but not *you is happy or *they am happy?
# Implement two solutions for the present tense paradigm of the verb be
# in English, first taking Grammar (8) as your starting point,
# and then taking Grammar (20) as the starting point.


import nltk
nltk.data.show_cfg('grammars/book_grammars/komar_ex_1.fcfg') #виводимо на екран створену граматику


  
# % start S
# # ###################
# # Grammar Productions
# # ###################
# # S expansion productions
# S -> NP[AGR=?n] VP[AGR=?n]
# # NP expansion productions
# NP[AGR=?n] -> N[AGR=?n]  
# # VP expansion productions
# VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
# # ###################
# # Lexical Productions
# # ###################
# #Створюємо правила граматики
# PropN[AGR=[NUM=sg, PER=1]] -> 'I'
# PropN[AGR=[NUM=sg, PER=2]] -> 'you'
# PropN[AGR=[NUM=sg, PER=3]] -> 'she'|'he'
# PropN[AGR=[NUM=pl, PER=3]] -> 'they'
# Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
# Cop[TENSE=pres, AGR=[NUM=sg, PER=2]] -> 'are'
# Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
# Cop[TENSE=pres, AGR=[NUM=pl, PER=3]] -> 'are'
# Adj -> 'happy'
