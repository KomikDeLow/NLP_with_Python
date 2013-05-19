#Presented by Tetiana Kobryn
#
#Chapter 7, Ex.1
#The IOB format categorizes tagged tokens as I, O, and B. Why are three tags
#necessary? What problem would be caused if we used I and O tags exclusively?

print """
The most widespread file representation uses IOB tags. In this scheme, each
token is tagged with one of three special chunk tags, I (inside), O (outside),
or B (begin). A token is tagged as B if it marks the beginning of a chunk.
If we used I and O tags exclusively, we wouldn't see the boundaries of
consecutive chunks."""
