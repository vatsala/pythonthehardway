from sys import argv

scriptname,filename=argv

print "So you want to see what I just wrote at %r" % filename

txt = file(filename,'r')

print txt.read()
txt.close()
