#Прокулевич К, ПРЛс-11, Розділ 9, Задача1
#What constraints are required to correctly parse word sequences like I am happy
#and she is happy but not *you is happy or *they am happy? Implement two solutions
#for the present tense paradigm of the verb be in English, first taking Grammar
#(8) as your starting point, and then taking Grammar (20) as the starting point.
#According to Grammar 8 verb be in present tense should be presented like:
#S -> P_SG1 VP_SG1
#S -> P_SG3 VP_SG3
#VP_SG1 -> V_SG1
#VP_SG3 -> V_SG3
#P_SG1 -> 'I'
#P_SG3 -> 'she'
#V_SG1 -> 'am'
#V_SG3 -> 'is'
# and according to Grammar 20:
#S -> NP[AGR=?n] VP[AGR=?n]
#NP[AGR=?n] -> PropN[AGR=?n]
#VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj

#PropN[AGR=[NUM=sg, PER=1]] -> 'I'
#Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
#Adj -> 'happy'

#PropN[AGR=[NUM=sg, PER=3]] -> 'she'
#Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
#Adj -> 'happy'
