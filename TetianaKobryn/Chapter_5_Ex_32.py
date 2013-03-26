# fine
#
# 32. Consult the documentation for the Brill tagger demo function, using
# help(nltk.tag.brill.demo). Experiment with the tagger by setting different values
# for the parameters. Is there any trade-off between training time (corpus size) and
# performance?


import nltk
nltk.tag.brill.demo(num_sents=200, max_rules=30, min_score=3)
# Brill accuracy: 0.736390
nltk.tag.brill.demo(num_sents=400, max_rules=30, min_score=3)
# Brill accuracy: 0.756728
nltk.tag.brill.demo(num_sents=600, max_rules=30, min_score=3)
# Brill accuracy: 0.772213


# The performance of the tagger is improving with increase of training time.
