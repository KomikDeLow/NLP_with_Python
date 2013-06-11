# Chapter_10_Ex_10_Fursachyk
import nltk
# initialize a Valuation with a list of pairs, each of which consists of a semantic symbol and a semantic value
val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
dom = set([])
m = nltk.Assignment(dom)
sem = nltk.Model(dom, val)
# experiment with evaluating different formulas of propositional logic
print sem.evaluate('(P & Q)', m)
True
print sem.evaluate('(P & P)', m)
True
print sem.evaluate('(V & P)', m)
Undefined

