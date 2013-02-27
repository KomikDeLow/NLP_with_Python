#Штангрет Ірина, ПРЛс-13, завдання 7
d1={}.fromkeys(['want', 'be', 'like']) # створила словник 1
 d2={}.fromkeys(['winter', 'summer', 'weather', 'girl', 'tiger'])# словник 2
d1.update(d2)#за допомогою функції update приєднала всі слова словника 2 до словника 1
sorted(d1)
['be', 'girl', 'like', 'summer', 'tiger', 'want', 'weather', 'winter']#словник 1 доповнився іншим

