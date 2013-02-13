# this formatter stands for raw output, usually the output of the reper() function
formatter = "%r %r %r %r"

# nothing unusual here
print formatter % (1,2,3,4)
# nothing unusual here too.
# Except that with the same formatter, we are able to print both numbers and strings
print formatter % ("one","two","three","four")
# there you go, now we are printing boolean data
print formatter % (True,False,False,True)
# using the formatter to pring the formatter
# this automatically wraps a single quote around every formatter group that gets printed. intriguing.
print formatter % (formatter,formatter,formatter,formatter)
# this one also wraps a single quote around every string. must be cause of the %r formatter
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didnt sing.",
	"So I said goodnight."
)
