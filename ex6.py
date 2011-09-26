# defines the variable x and puts a string '10' into the statement
x = "There are %d types of people." % 10

# nothing
binary = "binary"
do_not = "don't"

# defines the variable y and inserts the previous pointless variables within it (1)
y = "Those who know %s and those who %s." % (binary, do_not)

# puts all of the above together
print x
print y

# repeats the joke in case you're dumb
print "I said: %r." % x
print "I also said: '%s'." % y

# sets up variables called hilarious and joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# displays joke_evaluation in terms of hilarious (false)
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
