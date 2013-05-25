# Presented by Olha Truniak, ALs-13
# Chapter 8, Ex. 12

# We have seen that a chart parser adds but never removes edges from a chart. Why?


print """ Notice that we have not used any built-in parsing functions here. We’ve implemented
a complete primitive chart parser from the ground up! The chart data structure: Non-terminals
are represented as extra edges in the chart. WFSTs have several shortcomings. First, as you can
see, the WFST is not itself a parse tree, so the technique is strictly speaking recognizing
that a sentence is admitted by agrammar, rather than parsing it. Second, it requires every
non-lexical grammar production to be binary. Although it is possible to convert an arbitrary
CFG into this form, we would prefer to use an approach without such a requirement. Chart parsers
use a slightly richer data structure and some interesting algorithms to solve these problems"""
