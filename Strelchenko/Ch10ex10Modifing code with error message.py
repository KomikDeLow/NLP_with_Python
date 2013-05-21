# -*- coding: cp1251 -*-
import nltk
sent = 'Error. This word is not in domain model'
v = """
        bertie => b
        olive => o
        cyril =>
        boy => {b}
        girl => {o}
        dog => {c}
        walk => {o, c}
        see => {(b, o), (c, b), (o, c)} 
"""
# building a domain module
val = nltk.parse_valuation(v)
def eval(sem):            # building a function which valuate domain model
    if sem in v:
        m.evaluate(sem)
    else:
        print sent  # puting out error message

sem='see(olive)'
eval(sem)
