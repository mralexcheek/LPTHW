# imports the argv module so my argument is my variable
from sys import argv

# lists the variables that it needs to collect
script, haiku = argv

# user interface and confirmation
print "You've been writing some great haikus lately."
print "%r is a pretty good one." % haiku
print "Are you ready for me to share it with the world?"
print "If you are, press RETURN, if not hit CTRL-C."

# pauses the program waiting for the user to respond 
raw_input("?")

# announces the loading of the file
print "Here comes %r..." % haiku

#creates a new variable with the contents of the file
txt = open(haiku)
# and reads it
print txt.read()

#finally, closes the file
txt.close()
