>>> import nltk
>>> nltk.tag.brill.demo(num_sents=200, max_rules=30, min_score=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.740210]
Training bigram tagger:
    [accuracy: 0.736390]
Training Brill tagger on 160 sentences...
Finding initial useful rules...
    Found 338 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------
   3   3   0   0  | WDT -> IN if the tag of the following word is 'DT'

Brill accuracy: 0.736390
Done; rules and errors saved to rules.yaml and errors.out.




>>> nltk.tag.brill.demo(num_sents=400, max_rules=40, min_score=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.751346]
Training bigram tagger:
    [accuracy: 0.756728]
Training Brill tagger on 320 sentences...
Finding initial useful rules...
    Found 1243 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------
   3   3   0   0  | WDT -> IN if the tag of words i+1...i+2 is 'NNP'

Brill accuracy: 0.756728
Done; rules and errors saved to rules.yaml and errors.out.




>>> nltk.tag.brill.demo(num_sents=600, max_rules=40, min_score=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.768336]
Training bigram tagger:
    [accuracy: 0.771567]
Training Brill tagger on 480 sentences...
Finding initial useful rules...
    Found 2333 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------
   4   5   1   0  | WDT -> IN if the tag of the following word is 'DT'
   3   3   0   0  | NNPS -> NNP if the tag of words i-2...i-1 is 'CC'

Brill accuracy: 0.772213
Done; rules and errors saved to rules.yaml and errors.out.
