
import nltk
import nltk.corpus 
def evaluate_contribution_of_unigram_tagger(category='news', freq_threshold=2):
    """ Preprocess Brown News by replacing low-frequency words with UNK,
    train and evaluate a bigram tagger and evaluate the contribution of
    the unigram tagger and default tagger.

    :param category: words/news category we use from Brown Corpus.
    :param freq_threshold: threshold for word frequency. If freq is lower, word
                           will be replaced with 'UNK' (tag untouched). """
    
    # Build 'news' words frequency dictionary.
    freq_dict = nltk.FreqDist(nltk.corpus.brown.words(categories=category))

    # Get all words/tags from some category, replacing low-frequent words with 'UNK'.
    word_mapping = nltk.defaultdict(lambda: 'UNK')
    for word,tag in nltk.corpus.brown.tagged_words(categories=category):
        if freq_dict[word] > freq_threshold:
            # If word is high-frequent it won't be replaced with 'UNK'.
            word_mapping[word] = word

    # Now get default Brown tagged sentences and ours (with low-frequent words replacement).
    brown_tagged = nltk.corpus.brown.tagged_sents(categories=category)
    custom_tagged = []
    for sentence in nltk.corpus.brown.tagged_sents(categories=category):
        custom_tagged.append([(word_mapping[word], tag) for word, tag in sentence])

    # Prepare test/training data for training/evaluation.
    # We get 90% of data as training set, and 10% as test set.
    size  = int(len(brown_tagged) * 0.9)
    train_brown = brown_tagged[:size]
    test_brown = brown_tagged[size:]
    train_custom = custom_tagged[:size]
    test_custom = custom_tagged[size:]

    default_tagger = nltk.DefaultTagger('NN')
    # Train BigramTagger on Brown-tagged sentences, evaluate custom tagged sentences.
    unigram_tagger = nltk.UnigramTagger(train_brown, backoff=default_tagger)
    bigram_tagger = nltk.BigramTagger(train_brown, backoff=unigram_tagger)
    print "   Evaluating Brown tagged sentences using BigramTagger "\
          "trained on Brown data: %s" % (bigram_tagger.evaluate(test_brown),)

    # Vice versa. Train tagger on custom data and evaluate Brown data.
    unigram_tagger = nltk.UnigramTagger(train_custom, backoff=default_tagger)
    bigram_tagger = nltk.BigramTagger(train_custom, backoff=unigram_tagger)
    print "   Evaluating custom tagged sentences using BigramTagger "\
          "trained on custom data: %s" % (bigram_tagger.evaluate(test_custom),)

    # Use BigramTagger based on DefaultTagged directly.
    bigram_tagger = nltk.BigramTagger(train_custom, backoff=default_tagger)
    print "   Evaluating custom tagged sentences using BigramTagger trained on "\
          "custom data without UnigramTagger: %s" % \
          ((bigram_tagger.evaluate(test_custom)),)

print "\nEvaluating contribution of default tagger and unigram tagger:"
evaluate_contribution_of_unigram_tagger(category='news', freq_threshold=2)

