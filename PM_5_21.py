import nltk
# import Brown corpus
from nltk.corpus import brown
# explore words adore, like, love and prefer are used in texts
brown_learned_text = brown.words(categories='learned')
sorted (set(a for (a,b)in nltk.ibigrams(brown_learned_text) if b =='adore'))
[]
brown_learned_text = brown.words(categories='learned')
sorted (set(a for (a,b)in nltk.ibigrams(brown_learned_text) if b =='like'))
['(', ',', '--', ';', 'Papers', 'Surrealists', '``', 'a', 'anything', 'are', 'blow', 'boys', 'but', 'cities', 'countries', 'deceptively', 'devices', 'drawn', 'eggs', 'emotions', 'feel', 'felt', 'females', 'group', 'groups', 'instrument', 'is', 'kennings', 'labels', 'less', 'look', 'looked', 'looks', 'material', 'me', 'near-synonyms', 'not', 'of', 'painter', 'poems', 'press', 'quality', 'questions', 'remarkably', 'should', 'situations', 'societies', 'something', 'sounds', 'the', 'us', 'value', 'was', 'we', 'were', 'work', 'world', 'writers']
brown_learned_text = brown.words(categories='government')
sorted (set(a for (a,b)in nltk.ibigrams(brown_learned_text) if b =='prefer'))
['I']
brown_learned_text = brown.words(categories='government')
sorted (set(a for (a,b)in nltk.ibigrams(brown_learned_text) if b =='love'))
['His']
brown_learned_text = brown.words(categories='news')
sorted (set(a for (a,b)in nltk.ibigrams(brown_learned_text) if b =='like'))
[',', 'I', 'Motorists', 'We', 'acting', 'always', 'and', 'be', 'car', 'cities', "doesn't", 'equipment', 'feel', 'firms', 'girls', 'is', 'jangling', 'just', 'legislators', 'looked', 'looks', 'of', 'organizations', 'people', 'place', 'places', 'playing', 'seems', 'shaped', 'the', 'they', 'to', 'together', 'went', 'will', 'would']

