# -*- coding: utf-8 -*-
#Iryna Shtanhret, AL-13, chapter 10, task4
#Translate the following verb phrases using λ-abstracts and quantified formulas of first-order logic.
#feed Cyril and give a capuccino to Angus
#∀x.(feed(x,Cyril) ^ give(y,capuccino))
#λxλy.(feed(x) & give(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic =  λxλy.(feed(x) & give(y))'
print '-------------------------------------------------------------------------'

#b. be given ‘War and Peace’ by Pat
#∃x.(give(x,‘War and Peace’) ^ giveer(y,Pat))
#λxλy.(give(x) & giver(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic =  λxλy.(give(x) & giver(y))'
print '-------------------------------------------------------------------------'

#c. be loved by everyone
#∀x.(love(x) ^ lover(y,everyone))
#λxλy.(love(x) ^ lover(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic =  λxλy.(love(x) ^ lover(y))'
print '-------------------------------------------------------------------------'

#d. be loved or detested by everyone
#∀x.((love(x) ^ lover(y,everyone))|( detest(x) ^ detester(y,everyone))
#λxλy.((love(x) ^ lover(y))|( detest(x) ^ detester(y))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic =  λxλy.((love(x) ^ lover(y))|( detest(x) ^ detester(y))'
print '-------------------------------------------------------------------------'

#e. be loved by everyone and detested by no-one
#∀x.((love(x) ^ lover(y,everyone))^( detest(x) ^ detester(z,no-one))
#λxλyλz.((love(x) ^ lover(y))^( detest(x) ^ detester(z))
print 'sentence_A  =  feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic =  λxλyλz.((love(x) ^ lover(y))^( detest(x) ^ detester(z))'
print '-------------------------------------------------------------------------'



