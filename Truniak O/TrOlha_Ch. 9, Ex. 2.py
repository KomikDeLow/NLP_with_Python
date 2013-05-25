# Presented by Olha Truniak, ALs-13
# Ch.9, Ex.2

# Develop a variant of grammar in Example 9-1 that uses a feature COUNT to make
# the distinctions shown here:

# a. The boy sings. # here we have number case for noun+definite article(for expression the concretization)
# b. *Boy sings.

# a. The boys sing. # "the" usually indicates one or more items that are specific or unique.(about concrete boys)
# b. Boys sing.

# a. The water is precious. # "the" usually indicates one or more items that are specific or unique.
# underlining that the water is precious)
# b. Water is precious # if it is uncountable noun(here especially)


import nltk
nltk.data.show_cfg('grammars/book_grammars/feat1.fcfg')

"""
