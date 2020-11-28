myFile = open('test.txt')

# Reading a whole file
print(myFile.read())

# This will show empty because the file cursor is at the EOF after executing the above command
print(myFile.read())

# To position the cursor at starting point
myFile.seek(0)
contents = myFile.read()
print(contents)

myFile.seek(0)
# To get each line as elements in List
print(myFile.readlines())

# Closing an opened file
myFile.close()



# Another way of Reading file (Recommended Way)
with open('test.txt', mode='r') as fp:
    info = fp.read()
print(info)

# Writing on file
#   mode = w (write only, overwrite file/create new)
#   mode = a (append only)
#   mode = r+ (reading & writing)
#   mode = w+ (writing & reading)
with open('test.txt', mode='a') as fp:
    fp.write('\nAdded Fourth Line')

# It will create a new file when file name does not exists
with open('abc.txt', mode='a') as fp:
    fp.write('New file Created !!')
    



