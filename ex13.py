from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

answer = raw_input("Why'd you say that? ")
print "Ooooh! '%s,' you say? Think faster idiot!" % (answer) 
