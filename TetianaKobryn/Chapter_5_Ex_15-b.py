Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.corpus import brown
>>> tagged_words = brown.tagged_words(categories='adventure', simplify_tags=True)
>>> data = nltk.ConditionalFreqDist((word.lower(), tag)
                                    for (word, tag) in tagged_words)

>>> for word in data.conditions():
        if len(data[word]) > 3:
            tags = data[word].keys()
            print word, ' '.join(tags)

            
back ADV N V ADJ
even ADV V DET ADJ
hit VD V VN N
last DET ADV N V
left VD VN ADJ N
like CNJ V P ADJ
outside ADV ADJ N P
past P ADV ADJ DET N
right ADJ DET ADV N
spread V VD N VN
still ADV DET ADJ V
>>> 
