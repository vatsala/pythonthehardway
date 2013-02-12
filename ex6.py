#this is a variable declaration
x = "There are %d types of people." % 10
#this is another variable declaration
binary ="binary"
#yet another variable
do_not="don't"
#another variable with multiple variables inserted with format characters
y="Those who know %s and those who %s." % (binary, do_not)

#print the variables declared and constructed so far
print x
print y

#Show the use of %r and the use of single quotes within a string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# concatenate values of two variables using % symbol
print joke_evaluation % hilarious

w ="This is the left side of .."
e ="a string with a right side."

# concatenate values of two variables using + symbol
print w+e
