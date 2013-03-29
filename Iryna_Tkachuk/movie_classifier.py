# presented by Tkachuk Iryna
# PRLs 13
# Analyze_movie_classifier_with_word_net()

"""Classifier accuracy evaluation may differ each time we ran a script since
data split to training and test sets is shuffled randomly each time (that
results in different training/test sets).
"""

import nltk
import random

def __evaluate_accuracy(data, training_set_part=0.9):
    """ Splits all data into training_set and test_set and evaluates classifier accuracy.

    :param data: list of items containing training and test data.
    :param training_set_part: 0.0-1.0 - part of training set in data.
    """
    # Splitting data to training set and test set
    size = int(len(data) * training_set_part)
    # Mix data for better results.
    random.shuffle(data)
    training_set, test_set = data[:size], data[size:]
    # Build a classifier.
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    # Evaluating accuracy.
    acc = nltk.classify.accuracy(classifier, test_set)
    return acc

def __build_features_from_movie_reviews(words):
    """ Builds features list for classifier using words from moview_reviews. """
    features = []
    # Iterate on all review categories.
    for category in nltk.corpus.movie_reviews.categories():
        # For each category iterate on all reviews.
        for file_id in nltk.corpus.movie_reviews.fileids(category):
            # Get all words from movie review.
            review_words = [w.lower() for w in nltk.corpus.movie_reviews.words(file_id)]
            # Build a features dict - statistics if word is in movie review.
            f_words = [('contains(%s)' % w, w in review_words) for w in words]
            features.append((dict(f_words), category))

    return features


def analyze_movie_classifier_with_word_net():
    # Build a frequency distribution for all words in movie reviews.
    words = [word.lower() for word in nltk.corpus.movie_reviews.words()]
    words_freq_dist = nltk.FreqDist(words)
    # We take only 200 most frequent words.
    freq_words = words_freq_dist.keys()[:200]

    # Prepare feature set for building classifier.
    features = __build_features_from_movie_reviews(freq_words)
    base_accuracy = __evaluate_accuracy(features, 0.8)
    print "Number of words in base classifier - %s" % len(freq_words)
    print "Base accuracy - %s" % base_accuracy

    # Update the list of most frequent words.
    updated_freq_words = set(freq_words[:])
    # Look only after 200th word. No need to process already frequent words.
    # Check only next 100 words after most frequent. Too much of them to check all.
    # If we check more words here, e.g. 200:500, accuracy will increase in comparison
    # with base accuracy, in case in 200:300 it's much less possible.
    for word in words_freq_dist.keys()[200:300]:
        for synset in nltk.corpus.wordnet.synsets(word):
            for hypernym in synset.hypernyms():
                for l_name in hypernym.lemma_names:
                    # If words synonim is frequent (top 200) - add word to frequent too.
                    if l_name in freq_words and word not in updated_freq_words:
                        updated_freq_words.add(word)

    # Evaluate accuracy on updated set.
    features = __build_features_from_movie_reviews(updated_freq_words)
    accuracy = __evaluate_accuracy(features, 0.8)
    print "Number of words after wordnet update - %s" % len(updated_freq_words)
    print "Accuracy - %s" % accuracy
    
print "\nEvaluating classifier accuracy when using wordnet for synonims lookup:"
analyze_movie_classifier_with_word_net()
