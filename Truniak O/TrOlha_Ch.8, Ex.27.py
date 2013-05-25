# Presented by Olha Truniak, ALs-13

# Chapter 8, Ex.27

# Consider the algorithm in Example 8-3. Can you explain why parsing contextfree
# grammar is proportional to n3, where n is the length of the input sentence?

""" The algorithm can easily be converted into a parser, which has
the same bounds as the recognizer except that the space bound goes up
3 to n in order to store all the parses of very ambiguous grammars.
The time results we have obtained are only valid for a random
access model of a computer. The n3 result is the only one which
carries over to a Turing-machine-like model."""
