"""This is a personal note from the course: Python Data Structures in Coursera"""

# open()
""" 
handle = open(filename, mode)
-returns a handle use to manipulate the file
-filename is a string
-mode is optional and should be 'r' if we are planning 
to read the file and 'w' if we are going to write to the file.
ex) fhand=open('mbox.txt', 'r') 
"""

# newline 
""" 
use the newline character when we try to indecate the line ends.
-similar as \n in strings
"""

# file handle as a sequence
""" 
A file handle open for read can be treated as a sequence(an ordered set) 
of strings where each line in the file is a string in the sequence.
- able to iterate through a seqeunce by using 'for loop'
ex) file = open('mbox.txt')
    for x in file:
        print(x)   
"""

# Counting lines in a file
"""
file = open('mbox.txt')
count = 0
    for x in file:
        count = count + 1
print('Line count:', count)
"""


# searching through a file
"""
we can put an if statement in the for loop to only print some lines that meet our criteria
ex) file = open('mbox.txt')
    for x in file:
        if x.startwith('#'):
            print(x)
but this will add blank lines in between lines.
"""

# rstrip()
"""to remove whitespace from the right-hand side of the string.
ex) file = open('mbox.txt')
    for x in file:
        line = line.rstrip()
        if x.startwith('#'):
            print(x)
"""

# alternative: skipping with continue
""" or we can skip a line by using the continue statement.
ex) file = open('mbox.txt')
    for x in file:
        line = line.rstrip()
        if not x.startwith('#'):   # skip
            continue
        print(x)
"""

# another example
"""
file = input('Enter your file name: ')
handle = open(file)
count = 0
for line in handle:
    if line.startwith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', file)
"""


# bad file names
"""
file = input('Enter your junk file name: ')
try:
    handle = open(file)
except:
    print('File cannot be opened:', file)
    quit()
count = 0
for line in handle:
    if line.startwith('Subject:'):
        count = count + 1
print('There were', count, 'subject ilnes in', file)
"""