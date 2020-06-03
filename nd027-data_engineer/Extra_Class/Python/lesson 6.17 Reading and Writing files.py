# The open function returns a file object, which is a Python object through which 
# Python interacts with the file itself.
# path, read-only
f = open("some_file.txt", 'r')  
# This read method takes the text contained in a file and puts it into a string.
file_data = f.read() 
f.close()
print(file_data)

# write, append in the existing file
f = open('some_file.txt', 'a')
f.write('\ntry append this into some_file')

# write, but this will delete it contents
f = open('some_file.txt', 'w')

# this will create another file if it does not exist
f = open('another_file.txt', 'w')
f.write('Hello World!')
f.close()

# close after open!
files = []
for i in range(2):
    f = open('some_file.txt', 'r')
    files.append(f)  # object
    
    print(i)
    print(files)
    f.close()

# automatically close the file 
with open('some_file.txt', 'r') as f:
    file_date = f.read()
# still have access to contents after closing it
print(file_date)

# Calling the read Method with an Integer
with open('camelot.txt') as song:
    print(song.read(2))  # kept the 'window' at that position for the next call to read
    print(song.read(8))
    print(song.read())

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip()) # remove \ns which are newline characters in txt

print(camelot_lines)

# Quiz: Flying Circus Cast List
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt', 'r') as f:
    #use the for loop syntax to process each line
        for line in f:
    #and add the actor name to cast_list
            cast_list.append(line.split(",")[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
