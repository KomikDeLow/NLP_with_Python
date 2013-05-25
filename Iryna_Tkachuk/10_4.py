﻿#Presented by Iryna Tkachuk PRLs-13

# Translate the following verb phrases using λ-abstracts
# and quantified formulas of first-order logic.
		
"""a. feed Cyril and give a capuccino to Angus

λCyril.(feed(Cyril) ∧ give(capuccino, Angus)

λx.(feed(x) ∧ give(y, z)

b. be given ‘War and Peace’ by Pat

λPat.(give(Pat,book)

λx.(give(x,y)

c. be loved by everyone

∀x.(person(x)) –> ∃ z.(person(z)) ∧  love(x,z)

d. be loved or detested by everyone

∀x.(person(x)) –> ∃ z.(person(z)) ∧  love(x,z) ˅ destroy(x,z)

e. be loved by everyone and detested by no-one

∀x.(person(x)) –> ∃ z.(person(z)) ∧  love(x,z) ˄ ¬destroy(x,z)"""
