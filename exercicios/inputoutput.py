filepath_read = "pico.txt"
filepath_write = "outputpico.txt"
#i = 1 # start of iterator

#the 'open' function has two parameters, the first one is the path to the file
#you want to open, and second has a string with the letter "r" or "w", which means that
#we want to read the file.
with open(filepath_read, "r") as my_file:
    with open(filepath_write, "w") as my_file2:
        for line in my_file:
        #print(i) print the number of lines
            my_file2.write(line)
            #print(line) # print the contents of the file
            #i += 1 # increment number of lines
print("look inside your folder...")
my_file.close()
my_file2.close()