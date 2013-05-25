# Halyna Khimka
# Chapter 9.10
# Informal algorithm for unifying two feature structures

print """
1) Find identical features and when they have different paths -- unify them.
2) if there are identical paths - unify values where it is possible.
3) if there is a value for ?x in one path - insert the same values to other features which have the same ?x
4) if there are identical paths - 'make a link' using '(integer)'
"""
