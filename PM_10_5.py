import nltk
# parse the input into logical expressions 
lp = nltk.LogicParser()
# name a declaration of the value
e1 = lp.parse(r'exists y.love(pat,y)')
e2 = lp.parse('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
# display the result
print e3.simplify()
# result: there is some y whose is loved by pat 
e1 = lp.parse(r'exists y.love(pat,y)')
e2 = lp.parse(r'love(y,pat)')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print e3.simplify()
# result: there is some y whose is loved by pat and y love pat
e1 = lp.parse(r'walk')
e2 = lp.parse('fido')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print e3.simplify()
# result: fido walks
