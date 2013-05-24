# Presented by Tetiana Kobryn

# Chapter 10, Ex.4
# Translate verb phrases using λ-abstracts and quantified formulas
# of first-order logic.


"""
a. feed Cyril and give a capuccino to Angus
\x.\y.\z.(feed(x) & give(y, z))(Cyril, capuccino, Angus)

b. be given ‘War and Peace’ by Pat
\x.\y. (be_given(x, y)) (War and Peace, Pat)

c. be loved by everyone
\x. (be_loved(x))(everyone)

d. be loved or detested by everyone
\x. (be_loved(x) | be_detested(x))(everyone)

e. be loved by everyone and detested by no-one
\x. (be_loved(x) & -be_detested(x))(everyone)
"""


