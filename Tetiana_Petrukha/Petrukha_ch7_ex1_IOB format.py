# Petrukha Tetiana Als-11
# Chapter_7, Ex_1

# The IOB format categorizes tagged tokens as I, O, and B.
# Why are three tags necessary?
# What problem would be caused if we used I and O tags exclusively?

question1=('Question:')
print question1
question=('The IOB format categorizes tagged tokens as I, O, and B. Why are three tags necessary?What problem would be caused if we used I and O tags exclusively?')
print question
print ("-------------------------------------------------------------------------------")
answer1=('Answer:')
print answer1
answer=('IOB(Inside Outside Beginning) - a file representation format for tagging tokens in chunkingAs such, there is one token per line, each with its part of speech tagand tag block (chunk). This format allows us to represent more than one type of unit,until the pieces do not overlap. If it were not a tag B,we would not know that this is the beginning of the block.')
print answer

# Answer
# IOB(Inside Outside Beginning) - a file representation format for tagging tokens in chunking
# As such, there is one token per line, each with its part of speech tag
# and tag block (chunk). This format allows us to represent more than one type of unit,
# until the pieces do not overlap. If it were not a tag B,
# we would not know that this is the beginning of the block.
