Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> help(nltk.tag.brill.demo) #open help
Help on function demo in module nltk.tag.brill:

demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.8, trace=3)
    Brill Tagger Demonstration
    
    :param num_sents: how many sentences of training and testing data to use
    :type num_sents: int
    :param max_rules: maximum number of rule instances to create
    :type max_rules: int
    :param min_score: the minimum score for a rule in order for it to
        be considered
    :type min_score: int
    :param error_output: the file where errors will be saved
    :type error_output: str
    :param rule_output: the file where rules will be saved
    :type rule_output: str
    :param randomize: whether the training data should be a random subset
        of the corpus
    :type randomize: bool
    :param train: the fraction of the the corpus to be used for training
        (1=all)
    :type train: float
    :param trace: the level of diagnostic tracing output to produce (0-4)
    :type trace: int

>>> nltk.tag.brill.demo(num_sents=200, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.663753]
Training bigram tagger:
    [accuracy: 0.660202]
Training Brill tagger on 60 sentences...
Finding initial useful rules...
    Found 59 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------

Brill accuracy: 0.660202
Done; rules and errors saved to rules.yaml and errors.out.
>>> nltk.tag.brill.demo(num_sents=400, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.703992]
Training bigram tagger:
    [accuracy: 0.702983]
Training Brill tagger on 120 sentences...
Finding initial useful rules...
    Found 177 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------

Brill accuracy: 0.702983
Done; rules and errors saved to rules.yaml and errors.out.
#I changed the number of sentences (num_sents) used to train the tagger, first 200 sentences, then with 400. One can see that with a greater quantity of training sentences accuracy is improved from 0.660202 to 0.702983. 
>>> nltk.tag.brill.demo(num_sents=200, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.7, trace=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.758300]
Training bigram tagger:
    [accuracy: 0.754980]
Training Brill tagger on 140 sentences...
Finding initial useful rules...
    Found 324 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------

Brill accuracy: 0.754980
Done; rules and errors saved to rules.yaml and errors.out.
>>> nltk.tag.brill.demo(num_sents=400, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.7, trace=3)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.755286]
Training bigram tagger:
    [accuracy: 0.758059]
Training Brill tagger on 280 sentences...
Finding initial useful rules...
    Found 991 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------
   3   3   0   0  | WDT -> IN if the tag of the following word is 'DT'

Brill accuracy: 0.758752
Done; rules and errors saved to rules.yaml and errors.out.
#Now I changed the parameter "train" from 0.3 to 0.7, in order to use a larger portion of the corpus for training the tagger. Accuracy improved by 5-9% (from 0.660202 to 0.754980 with 200 sentences, and from 0.702983 to 0.758752 for 400 sentences). It's interesting to observe that with the greater "train" value accuracy does not depend on the number of sentences (with 200 sentences and "train = 0,7" and 400 sentences with "train = 0.7" accuracy is 0.754980 and 0.758752).
#I attempted changing other parameters such as "min_score," "randomize," and "trace." Changing "min_score" and "trace" didn't yield any results, and "randomize" gave an error.   
>>> 
