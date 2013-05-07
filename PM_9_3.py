# TODO
# Comments?
#
import nltk
fs1 = nltk.FeatStruct("[A = [D = d]]")
fs2 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
fs1.subsumes(fs2)
True
def subs():
	if fs1.subsumes(fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes(fs1):
		print fs1.unify(fs2)
	else:
		print "This two structures are not incommensurable"
