#Write a program to find those verbs in the PP Attachment Corpus nltk.corpus.ppattach.
# Find any cases where the same verb exhibits two different attachments,
#but where the first noun, or second noun, or preposition stays unchanged
#(as we saw in our discussion of syntactic ambiguity in Section 8.2).

import nltk
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries: #choice of verb determines whether the prepositional phrase is attached to the VP or to the NP.
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)

#review vocabulary and output text
for key in sorted(table):
    if len(table[key]) > 1:
        print key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V'])
