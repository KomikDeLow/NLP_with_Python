# by Ivanna Kushniruk
import nltk
lp = nltk.LogicParser()
e = lp.parse(r'\x.\y.\z.(feed(x) & give(y, z))(Cyril, capuccino, Angus)')
print 'feed Cyril and give a capuccino to Angus'
print e.simplify()
print ''
e = lp.parse(r'\x.\y.(be_given(x, y)) (War_and_Peace, Pat)')
print 'be given ‘War and Peace’ by Pat'
print e.simplify()
print ''
e = lp.parse(r'\x.(be_loved(x))(everyone)')
print 'be loved by everyone'
print e.simplify()
print ''
e = lp.parse(r'\x.(be_loved(x) | be_detested(x))(everyone)')
print 'be loved or detested by everyone'
print e.simplify()
print ''
e = lp.parse(r'\x.(be_loved(x) & be_detested(x))(everyone)')
print 'be loved by everyone and detested by no-one'
print e.simplify()


