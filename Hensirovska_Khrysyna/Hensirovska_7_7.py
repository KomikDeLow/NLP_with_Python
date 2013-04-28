#√енс≥ровська ’ристина,ѕ–Ћс-12
#розд≥л 7,завданн€ 7
#Carry out the following evaluation tasks for any of the chunkers you have developed
#earlier. (Note that most chunking corpora contain some internal inconsistencies,
#such that any reasonable rule-based approach will produce errors.)
#a. Evaluate your chunker on 100 sentences from a chunked corpus, and report
#the precision, recall, and F-measure.
#b. Use the chunkscore.missed() and chunkscore.incorrect() methods to identify
#the errors made by your chunker. Discuss.
#c. Compare the performance of your chunker to the baseline chunker discussed
#in the evaluation section of this chapter.
#import nltk
#from nltk.corpus import conll2000
#ѕишемо шаблон дл€ регул€рного виразу
#grammar="NP: {<DT|IN|PRP|NN>?<VBG><DT>?<NN>*}"
#—творюЇмо синтаксичний анал≥затор chunk.÷е готовий клас,€кий створюЇ
#екземи,вид≥л€Ї ≥менников≥ вирази
#cp=nltk.RegexpParser(grammar)
#We start off byestablishing a baseline for the trivial chunk parser cp that
#creates no chunks
#test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP'])
#print cp.evaluate(test_sents)
#sentence='His mother asks him cooking'
#sentence=sentence.split()
#Now that weТve defined our feature extractor, we can use it to train
#tagged=nltk.pos_tag(sentence)
#result=cp.parse(tagged)
#print result
#identify the errors made by my chunker
#The chunks which were included in the guessed chunk structures, but not in
#the correct chunk structures, listed in input order. 
   	# print chunk
#chunkscore = nltk.chunk.ChunkScore()
#The chunks which were included in the correct chunk structures, but not in
#the guessed chunk structures, listed in input order.
#chunkscore.score(test_sents,result)
#for chunk in chunkscore.incorrect():
	#print chunk
#for chunk in chunkscore.missed():
	#print chunk
