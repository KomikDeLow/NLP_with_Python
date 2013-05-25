#Translate sentences into predicate-argument formulas of first-order logic.
print "a) Angus likes Cyril and Irene hates Cyril."
print "like(Angus, Cyril) & hate(Irene, Cyril)"

print "b) Tofu is taller than Bertie."
print "be_taller(Tofu, Bertie)"

print "c) Bruce loves himself and Pat does too."
print "love(Bruce, Bruce) & love (Pat, Pat)"

print "d) Cyril saw Bertie, but Angus didn’t."
print "saw(Cyril, Bertie) & -saw(Angus, Bertie)"

print "e) Cyril is a four-legged friend."
print "is(Cyril, dog)"

print "f) Tofu and Olive are near each other."
print "be_near(T, O) & be_near(O, T)"
