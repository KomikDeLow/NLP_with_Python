<<<<<<< HEAD
# Petrukha Tetiana Als-11
# Chapter_5, Ex_13

# We can use a dictionary to specify the values to be substituted into a formatting string.
# Read Python’s library documentation for formatting strings (http://docs.python.org/lib/typesseq-strings.html)
# and use this method to display today’s date in two different formats.

=======
>>>>>>> parent of 772060a... Chapter 5_ex 13
# TODO
# comments ??
#

import datetime
now=datetime.date.today().strftime("%B %d, %Y")
print now
today=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
print today
