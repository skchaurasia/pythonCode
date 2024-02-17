#!/usr/bin/python3

# open(file, mode)
#file: The name (and path, if necessary) of the file you want to open.
#mode: if we use mode as w it will override the existing file so better to use mode as a to append file if exists

file = open('example.txt', 'a')
file.close()

# Output:
# Opens 'example.txt' in append mode, in the current directory. If the file does not exist, it will be created.

