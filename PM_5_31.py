# Modify the program in Example 5-4 to use a logarithmic scale on the x-axis, by replacing pylab.plot() with pylab.semilogx()
import nltk
import pylab
# arrange the sizes of the taggers and explore them
sizes=2**pylab.arange(15)
pylab.plot(sizes, '-bo')
pylab.title ('Lookup Tagger Performance with Varying Model Size')
pylab.xlabel('Model Size')
pylab.ylabel('Performance')
# display results
pylab.show()
# replace pylab.plot() with pylab.semilogx()
pylab.semilogx(sizes, '-bo')
pylab.title ('Lookup Tagger Performance with Varying Model Size')
pylab.xlabel('Model Size')
pylab.ylabel('Performance')
# display results
pylab.show()
