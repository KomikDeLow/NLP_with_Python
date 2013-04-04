import nltk
e=nltk.defaultdict(list)
def dic (headword,part of speech, sense, example):
    e[headword]=[part of speech,sense,example]
    dic ('plane','N','An airplane or hydroplane.')
    dic ('moustache','N','The unshawed growth of hair on the upper lip and sometimes down the sides of the mouth.')
    print e ['bird']
