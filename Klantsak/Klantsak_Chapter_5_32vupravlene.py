# TODO
# Коментарі! Що програма робить?
# Потрібно провести декілька експериментів з різними значеннями аргументів

# Veronika KLantsak ALs-11
#  Experiment with the tagger by setting different values
# for the parameters. Is there any trade-off between training time (corpus size) and
# performance?
import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.4, trace=4)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.6, trace=4)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.9, trace=4)
# With the increase in size of the corpus to process slows the implementation process
