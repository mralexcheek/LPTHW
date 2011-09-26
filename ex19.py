# defining the cheese_and_crackers function and the arguments it takes.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %r cheeses!" % cheese_count
    print "You have %r boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
# adds a new line
    print "Get a blanket.\n"

# runs the function with a certain set of numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# defines the variables that the function will use
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print "Finally, we can get the user to tell us the numbers:"
amount_of_cheese = raw_input("How many cheeses do you have? ")
amount_of_crackers = raw_input("How many boxes of crackers do you have? ")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
