

#% start S

Grammar Productions

S expansion productions
S -> NP[NUM=?n] VP[NUM=?n]
S -> NP[NUM=?n,COUNT=?C] VP[NUM=?n]
NP expansion productions
NP[NUM=?n] -> N[NUM=?n]
NP[NUM=?n,COUNT=?C] -> Det[COUNT=?C] N[NUM=?n]
NP[NUM=pl] -> N[NUM=pl]
VP expansion productions
VP[TENSE=?t, NUM=?n] -> V[TENSE=?t, NUM=?n]
VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj

Lexical Productions

Det[COUNT=def] -> 'the' 
N[NUM=sg] -> 'boy' | 'water' 
N[NUM=pl] -> 'boys' 
V[TENSE=pres, NUM=sg] -> 'sing' 
V[TENSE=pres, NUM=pl] -> 'sings'
Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
Adj -> 'precious'

# В англійській мові є визначені артикль 'the', який служить для визначення
# іменника і невизначений артикль 'a' ('an' перед голосними), що вказує
# на невизначений іменник

# В наступних прикладах можемо бачити у 3-х випадках 'а.' конкретизацію, а
# випадки 'b.' і граматично неправильними.

# Перед незліченними іменниками, що означають речовину чи масу, якщо не
# вказується кількість цієї речовини, то артикль не вживається.

# a. The boy sings.
# b. *Boy sings.

# a. The boys sing.
# b. Boys sing.

# a. The water is precious.
# b. Water is precious.
