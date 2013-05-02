import nltk
books=nltk.defaultdict(list)
def mydic (headword, part_of_speech, sense, example):
	books[headword]=[part_of_speech, sense, example]

mydic('dictionary', 'N', 'is a collection of words in one or more specific languages, often listed alphabetically (or by radical and stroke for ideographic languages), with usage information, definitions, etymologies, phonetics, pronunciations, and other information', 'The earliest dictionaries in the English language were glossaries of French, Italian or Latin words along with definitions of the foreign words in English.')
mydic('magazine', 'N', ' publications that are printed with ink on paper, and generally published on a regular schedule and containing a variety of content', 'The oldest consumer magazine still in print is The Scots Magazine, which was first published in 1739.')
mydic('novel', 'N', 'a long prose narrative that describes fictional characters and events in the form of a sequential story, usually', 'Don Quixote is the greatest novel of all time.')
mydic ('comics', 'N', 'an artistic medium in which images incorporate text or other visual forms of information in order to express a narrative or idea', 'The 1938 success of Action Comics and its lead hero Superman marked the beginning of the Golden Age of comic books, in which the superhero genre was most prominent.')
mydic('trilogy', 'N', 'a set of three works of art that are connected, and that can be seen either as a single work or as three individual works', 'Most trilogies are works of fiction involving the same characters or setting, such as The Deptford Trilogy.')
books['magazine']
['N', ' publications that are printed with ink on paper, and generally published on a regular schedule and containing a variety of content', 'The oldest consumer magazine still in print is The Scots Magazine, which was first published in 1739.']

