# Halyna Khimka
# FirstOrderLogic
# Chapter 10.2

print 'a) Angus likes Cyril and Irene hates Cyril'
print 'like(Angus, Cyril) & hate(Irene, Cyril)'

print 'b) Tofu is taller than Bertie'
print 'taller(Tofu, Bertie)'
# It can be interpreted as taller(Tofu,Bertie) & smaller(Bertie, Tofu)
# This information flows out from this sent but it is not obvious.
print 'taller(Tofu,Bertie) & smaller(Bertie, Tofu)'

print 'c) Bruce loves himself and Pat does too.'
print 'love(Bruce, Bruce)(Pat,Bruce)' # Is such formula possible? 
print 'love(Bruce, Bruce) & love(Pat, Bruce)'

print 'd) Cyril saw Bertie, but Angus didn’t.'
print 'see(Cyril, Angus) & -see(Angus, Bertie)'

print 'e) Cyril is a four-legged friend.'
print 'is(Cyril, friend) & is(Cyril, four-legged)'
print 'is(Cyril, friend) & has(Cyril, legs) & number(legs, four)'

print 'f)Tofu and Olive are near each other.'
print 'is(Tofu) and is(Olive) and near(Tofu, Olive) and near(Olive, Tofu)'
