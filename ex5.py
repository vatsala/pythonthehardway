name="Zed A. Shaw"
age=35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes= 'Blue'
teeth ='White'
hair='Brown'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d %d, and %d I get %d." % (age,height,weight,age+height+weight)
#Study Drills
# python format characters
#%s - printing string
#%r - print the stringified version of an object, the result of calling repr() function on it
# %d,%i - signed integer
# %f,%F - floating point decimal
# %e,%E - floating point exponential form
# %x,%X - signed hexadecimal
