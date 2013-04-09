# Halyna Khimka
# Chapter 7.1
#
# The IOB format categorizes tagged tokens as I, O, and B.
# Why are three tags necessary?
# What problem would be caused if we used I and O tags exclusively?
#

print " The IOB format categorizes tagged tokens as I, O, and B. \n Why are three tags necessary? \n What problem would be caused if we used I and O tags exclusively?"
print "  "
print "\t*********************"
print '\tAnswer:'
print " The most widespread file representation uses IOB tags. \n It means that each token is tagged with one of three special chunk tags, I (inside), O (outside), or B (begin).If we used only I and O tags we would meet the problem with the merges of chunks. \n B-tag marks the beggining of chunk. \n And if we didn't use this tag we wouldn't see the beggining of the second consecutive chunk. "
print "\t*********************"
