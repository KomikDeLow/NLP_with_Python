# Andrew Melnyk ALs-12

# Подившись у Help властивості nltk.tag.brill.demo налаштовую його і перевіряю резульатти роботи.
import nltk
nltk.tag.brill.demo(num_sents=150, max_rules=30,  min_score=3, error_output='errors.out', rule_output='rules.yaml', trace=4, train=0.9)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.768638]
Training bigram tagger:
    [accuracy: 0.776350]
Training Brill tagger on 135 sentences...
Finding initial useful rules...
    Found 324 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------

Brill accuracy: 0.776350
Done; rules and errors saved to rules.yaml and errors.out.

nltk.tag.brill.demo(num_sents=150, max_rules=30,  min_score=3, error_output='errors.out', rule_output='rules.yaml', trace=4, train=0.5)
Loading tagged data... 
Done loading.
Training unigram tagger:
    [accuracy: 0.682594]
Training bigram tagger:
    [accuracy: 0.675280]
Training Brill tagger on 75 sentences...
Finding initial useful rules...
    Found 78 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------

Brill accuracy: 0.675280
Done; rules and errors saved to rules.yaml and errors.out.

# Точність аналізатора є більшою коли час тренування є більшим.
