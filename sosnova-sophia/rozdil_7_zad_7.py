#Chapter 7 ex.7
import nltk
 from nltk.corpus import conll2000
 grammar="NP: {<DT|IN|PRP|NN>?<VBG><DT>?<NN>*}" # creating rules for grammar
 cp=nltk.RegexpParser(grammar) # creating a Chunk parcer
 test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP']) # evaluating the work of a chunker 
 print cp.evaluate(test_sents)

 sentence='The big dog walked out of the yard'
 sentence=sentence.split()
 tagged=nltk.pos_tag(sentence)
 result=cp.parse(tagged)
 print result

 chunkscore = nltk.chunk.ChunkScore()
 chunkscore.score(test_sents,result)
 for chunk in chunkscore.incorrect(): # chunks which are included in the guesssed chunk structure are not included in the correct chunk structures
	print chunk

	
 for chunk in chunkscore.missed(): # chunks which are included in the correct chunk structure are not included in the guessed chunk structures
	print chun
