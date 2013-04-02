# fine but accuracy?
#
# presented by Tkachuk Iryna
# PRLs 13
# Build a consecutive classifier for labeling dialogue acts.

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

def build_classifier_for_labeling_dialogue():
    """ Builds classifier for labeling dialogue acts. """
    # Get some chatting data from nltk corpus.
    chat_posts = nltk.corpus.nps_chat.xml_posts()

    # Convert posts to NaiveBayesClassifier acceptable format
    # Don't forget about previous post type field.
    features = []
    previous_post_class = None
    for post in chat_posts:
        # We split post into words using word_tokenize.
        # For each word we set a feature "contains(%word%)" to True
        # But before that post should be converted to string.
        text = ''.join(post.itertext())
        post_class = post.get('class')
        words = [("contains(%s)" % w.lower(), True) for w in nltk.word_tokenize(text)]
        f = dict(words)
        # Add one more feature - previous post class.
        f["prev-class"] = previous_post_class if previous_post_class else ''
        features.append((f, post_class))
        # Save post class as previous for next one.
        previous_post_class = post_class

    acc = __evaluate_accuracy(features, 0.9)
    return acc    
print "\nBuilding classifier for chat posts that considers previous post and " \
          "evaluating it's accuracy:"
print build_classifier_for_labeling_dialogue()
