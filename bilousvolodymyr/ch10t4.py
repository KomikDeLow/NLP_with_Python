# Bilous Volodymyr AL-11
# Chapter 10, task 4

#Translate the following verb phrases using ?-abstracts and quantified formulas of first-order logic.

#a. feed Cyril and give a capuccino to Angus
#?x.(feed(x,Cyril) ^ give(y,capuccino))
#?x?y.(feed(x) & give(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print '?-abstracts formulas of first-order logic =  ?x?y.(feed(x) & give(y))'
print '-------------------------------------------------------------------------'

#b. be given ‘War and Peace’ by Pat
#?x.(give(x,‘War and Peace’) ^ giveer(y,Pat))
#?x?y.(give(x) & giver(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print '?-abstracts formulas of first-order logic =  ?x?y.(give(x) & giver(y))'
print '-------------------------------------------------------------------------'

#c. be loved by everyone
#?x.(love(x) ^ lover(y,everyone))
#?x?y.(love(x) ^ lover(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print '?-abstracts formulas of first-order logic =  ?x?y.(love(x) ^ lover(y))'
print '-------------------------------------------------------------------------'

#d. be loved or detested by everyone
#?x.((love(x) ^ lover(y,everyone))|( detest(x) ^ detester(y,everyone))
#?x?y.((love(x) ^ lover(y))|( detest(x) ^ detester(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print '?-abstracts formulas of first-order logic =  ?x?y.((love(x) ^ lover(y))|( detest(x) ^ detester(y))'
print '-------------------------------------------------------------------------'

#e. be loved by everyone and detested by no-one
#?x.((love(x) ^ lover(y,everyone))^( detest(x) ^ detester(z,no-one))
#?x?y?z.((love(x) ^ lover(y))^( detest(x) ^ detester(z))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print '?-abstracts formulas of first-order logic =  ?x?y?z.((love(x) ^ lover(y))^( detest(x) ^ detester(z))'
print '-------------------------------------------------------------------------'
