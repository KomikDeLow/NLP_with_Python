import nltk
help(nltk.tag.brill.demo) #open help
nltk.tag.brill.demo(num_sents=200, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
nltk.tag.brill.demo(num_sents=400, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
#I changed the number of sentences (num_sents) used to train the tagger, first 200 sentences, then with 400. One can see that with a greater quantity of training sentences accuracy is improved from 0.660202 to 0.702983.
nltk.tag.brill.demo(num_sents=200, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.7, trace=3)
nltk.tag.brill.demo(num_sents=400, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.7, trace=3)
#Now I changed the parameter "train" from 0.3 to 0.7, in order to use a larger portion of the corpus for training the tagger. Accuracy improved by 5-9% (from 0.660202 to 0.754980 with 200 sentences, and from 0.702983 to 0.758752 for 400 sentences). It's interesting to observe that with the greater "train" value accuracy does not depend on the number of sentences (with 200 sentences and "train = 0,7" and 400 sentences with "train = 0.7" accuracy is 0.754980 and 0.758752).
#I attempted changing other parameters such as "min_score," "randomize," and "trace." Changing "min_score" and "trace" didn't yield any results, and "randomize" gave an error.
