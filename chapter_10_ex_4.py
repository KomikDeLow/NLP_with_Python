# Iuliia Tsymbalista

# Chapter 10, Ex.4
# Translate verb phrases using ?-abstracts and quantified formulas
# of first-order logic.

import nltk
lp = nltk.LogicParser()

#a. feed Cyril and give a capuccino to Angus
#\x.\y.\z.(feed(x) & give(y, z))(Cyril, capuccino, Angus)
e = lp.parse(r'\x.\y.\z.(feed(x) & give(y, z))(Cyril, capuccino, Angus)')
print 'example a:', e
print e.simplify() 


# b. be given ‘War and Peace’ by Pat
#\x.\y.(be_given(x, y)) (War and Peace, Pat)
e = lp.parse(r'\x.\y.(be_given(x, y)) (War_and_Peace, Pat)')
print 'example b:', e
print e.simplify() 


#c. be loved by everyone
#\x.(be_loved(x))(everyone)
e = lp.parse(r'\x.(be_loved(x))(everyone)')
print 'example c:', e
print e.simplify() 


#d. be loved or detested by everyone
#\x.(be_loved(x) | be_detested(x))(everyone)
e = lp.parse(r'\x.(be_loved(x) | be_detested(x))(everyone)')
print 'example d:', e
print e.simplify()


#e. be loved by everyone and detested by no-one
#\x.\y.(be_loved(x) & be_detested(y))(everyone)
e = lp.parse(r'\x.(be_loved(x) & be_detested(x))(everyone)')
print 'example e:', e
print e.simplify()

