#Maryna Ivaniv PRLs-11 Chapter 5 Ex.32
#Consult the documentation for the Brill tagger demo function,
#using help(nltk.tag.brill.demo). Experiment with the tagger
#by setting different values for the parameters. Is there any
#trade-off between training time (corpus size) and performance?

import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out',
                    rule_output='rules.yaml', randomize=False, train=0.80000000000000004, trace=3)
nltk.tag.brill.demo(num_sents=1000, max_rules=20, min_score=30, error_output='errors.out',
                    rule_output='rules.yaml', randomize=False, train=0.80000000000000004, trace=4)
nltk.tag.brill.demo(num_sents=100, max_rules=100, min_score=30, error_output='errors.out',
                    rule_output='rules.yaml', randomize=False, train=0.80000000000000004, trace=1)
nltk.tag.brill.demo(num_sents=2000, max_rules=100, min_score=3, error_output='errors.out',
                    rule_output='rules.yaml', randomize=False, train=0.800000000000004, trace=5)

#In this program we found Brill accuracy , maximum number of rules, the minimum score for a rule
#the fraction of the the corpus and the level of diagnostic tracing output
