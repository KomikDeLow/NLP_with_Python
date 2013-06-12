# Chapter_10_Ex_4_Mokhonova
import nltk
lp = nltk.LogicParser()

#a. feed Cyril and give a capuccino to Angus
e = lp.parse(r'\x.\y.\z.(feed(x) & give(y, z))(Cyril, capuccino, Angus)')
print 'example a:', e
print e.simplify() 

# b. be given ‘War and Peace’ by Pat
e = lp.parse(r'\x.\y.(be_given(x, y)) (War_and_Peace, Pat)')
print 'example b:', e
print e.simplify() 

#c. be loved by everyone
e = lp.parse(r'\x.(be_loved(x))(everyone)')
print 'example c:', e
print e.simplify() 

#d. be loved or detested by everyone
e = lp.parse(r'\x.(be_loved(x) | be_detested(x))(everyone)')
print 'example d:', e
print e.simplify()

#e. be loved by everyone and detested by no-one
e = lp.parse(r'\x.(be_loved(x) & be_detested(x))(everyone)')
print 'example e:', e
print e.simplify()

