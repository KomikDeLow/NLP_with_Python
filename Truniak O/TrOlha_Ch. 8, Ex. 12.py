# Presented by Olha Truniak, ALs-13
# Chapter 8, Ex. 12

# We have seen that a chart parser adds but never removes edges from a chart. Why?


print """ Chart parsers use a set of rules to heuristically decide when an edge
should be added to a chart. This set of rules, along with a specification of when
they should be applied, forms a strategy. One rule is particularly important, since 
it is used by every chart parser: the Fundamental Rule. This rule is used to combine
an incomplete edge that's expecting a nonterminal B with a following, complete edge 
whose left hand side is B. 
Fundamental Rule
If the chart contains the edges
  [A → α • B β , (i, j)]
  [B → γ • , (j, k)]
then add the new edge
  [A → α B • β , (i, k)]
where α, β, and γ are (possibly empty) sequences of terminals or non-terminals.
Note that the dot has moved one place to the right, and the span of this new edge is 
the combined span of the other two. Note also that in adding this new edge we do not 
remove the other two, because they might be used again."""
