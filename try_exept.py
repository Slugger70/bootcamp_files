filename = "test2.csv"
default_file = "rodents.csv"
try:
    file = open(filename)
except IOError as e:
    print e
    file = open(default_file)
except:
    print "There was some other kind of error"
    raise
    
print file.readline()
