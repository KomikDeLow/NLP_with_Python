# Bahen Diana, PRLs-11, Chapter 10, Exercise 4

#a. feed Cyril and give a capuccino to Angus
#∀x.(feed(x,Cyril) ^ give(y,capuccino))
#λxλy.(feed(x) & give(y))
print 'sentence_A = feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic = λxλy.(feed(x) & give(y))'

#b. be given ‘War and Peace’ by Pat
#∃x.(give(x,‘War and Peace’) ^ giveer(y,Pat))
#λxλy.(give(x) & giver(y))
print 'sentence_A = feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic = λxλy.(give(x) & giver(y))'

#c. be loved by everyone
#∀x.(love(x) ^ lover(y,everyone))
#λxλy.(love(x) ^ lover(y))
print 'sentence_A = feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic = λxλy.(love(x) ^ lover(y))'

#d. be loved or detested by everyone
#∀x.((love(x) ^ lover(y,everyone))|( detest(x) ^ detester(y,everyone))
#λxλy.((love(x) ^ lover(y))|( detest(x) ^ detester(y))
print 'sentence_A = feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic = λxλy.((love(x) ^ lover(y))|( detest(x) ^ detester(y))'

#e. be loved by everyone and detested by no-one
#∀x.((love(x) ^ lover(y,everyone))^( detest(x) ^ detester(z,no-one))
#λxλyλz.((love(x) ^ lover(y))^( detest(x) ^ detester(z))
print 'sentence_A = feed Cyril and give a capuccino to Angus'
print 'λ-abstracts formulas of first-order logic = λxλyλz.((love(x) ^ lover(y))^( detest(x) ^ detester(z))'