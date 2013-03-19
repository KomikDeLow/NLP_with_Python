# TODO
# Comments ?
#  Experiment with the tagger by setting different values
# for the parameters. Is there any trade-off between training time (corpus size) and
# performance?
import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=90, max_rules=100,  min_score=4, trace=7, train=0.9)
