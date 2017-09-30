#!python

from sys import argv
script, file_name = argv

#file_name = raw_input("Pls input file name:")

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

print "read %s context" % file_name
current_file = open(file_name)
print_all(current_file)

print "now let's rewind,kind of like a tape"
rewind(current_file)

print "lst's print three line"
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
