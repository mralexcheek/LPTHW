# imports the argv module
from sys import argv

# names the variables: the script's name and the filename user wants to use
script, filename = argv

# opens the file and makes that the value for the variable 'txt'
txt = open(filename)

# announces the file about to be opened 
print "Here's your file %r:" % filename
# prints the contents of the txt variable, now the file
print txt.read()

# asks for the filename again
print "Type the filename again:"

# creates a new variable with the filename from the user's input
file_again = raw_input("> ")

# creates a new variable associated with the contents of the file
txt_again = open(file_again)

#prints the contents of the variable
print txt_again.read()



