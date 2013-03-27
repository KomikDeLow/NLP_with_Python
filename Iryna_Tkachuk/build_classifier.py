    # presented by Iryna Tkachuk
    # PRLc 13

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


def build_classifier():
    """ Build a classifier based on corpus senseval data and eval it's accuracy. """
    # Load senseval instances.
    instances = nltk.corpus.senseval.instances('serve.pos')

    # Instances are of incorrect format. For training classifier we need
    # list of tuples (features dictionary, senses string).
    # Each instance has attributes "word", "position", "context" and "senses".
    # We will combine "word", "position", "context" into features dictionary and
    # join all "senses" into one string.
    features = []
    for inst in instances:
        # Converting strings in "context" to (string, "None") tuples, so that we can create dict
        context = [c if isinstance(c, tuple) else (c, "None") for c in inst.context]
        # Creating dict.
        f = dict(context)
        # Updating features "word" and "position"
        f.update({"word": inst.word, "position": inst.position})
        features.append((f, ' '.join(inst.senses)))

    acc = __evaluate_accuracy(features, 0.9)
    return acc
if __name__ == '__main__':
    print "Building NaiveBayesClassifier for Senseval data and evaluating accuracy: "
    print build_classifier()


