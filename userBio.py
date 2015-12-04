import string
import random
import sys

print "This program saves your bio in a text file with your name. This eventually with more implementation will save your data to an array, however that part has not been created yet. Below you will be prompted for more info"

name2 = raw_input('Enter your name (no spaces)')+'.txt'
bio = raw_input('Enter what you want in your bio: ')

with open(name2, "w") as text_file:
	text_file.write(bio)
	
print "Thank you, your file has been updated/created"
