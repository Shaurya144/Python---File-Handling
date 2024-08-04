# Delete files
import os
os.remove("demofile.txt")

f = open("demofile.txt", "rt")

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exist

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

#open and read the file after the appending
f = open("demofile2.txt", "r")
print(f.read())

