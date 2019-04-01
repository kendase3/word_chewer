#! /usr/bin/env python 

# Copyright (c) 2010 Steve E. Kendall <ira@wereware.com> 
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import sys 

FILENAME = "/usr/share/dict/words" 
PROGRAM_NAME = "word_chewer.py" 
HELP_PROMPT =  "Usage:\n%s\t\t\t\t\t(to use defaults)\n%s [victim_word]\t\t\t(to supply word initially)\n%s [victim_word] [dictionary]\t(to supply word and path to custom dictionary file)\n" % (PROGRAM_NAME, PROGRAM_NAME, PROGRAM_NAME)

ASCII_OFFSET = 97

def get_key(str_in):
	"""
		Generates a unique key for any anagram match, 
			given a certain word length.  Will not generate
			indicative keys if comparing words of different lengths	
	"""
	key = 0
	for char in str_in.lower():
		# character's index from 'a'
		offset = ord(char) - ASCII_OFFSET 
		num_letters = len(str_in) 
		# ** is exponent operator
		key += (num_letters ** offset) 
		
	return key

### main ###

# handle input 
input = "" 

if len(sys.argv) == 1:
	input = raw_input("Word to be chewed: ") 

else: 
	if sys.argv[1] == "help":
		print HELP_PROMPT
		exit() 
	else:
		input = sys.argv[1] 

if len(sys.argv) > 2:
	filename = sys.argv[2]
else:
	filename = FILENAME

if len(sys.argv) > 3:
	print HELP_PROMPT   
	exit()

input_key = get_key(input)

try:
	input_file = open(filename, 'r')
except IOError:
	print "\n###ERROR###\nInvalid dictionary file provided.  Run 'python %s help' to list syntax of manually supplying dictionary file." % PROGRAM_NAME 
	exit()
match_list = []
cur_line = 'throwaway'
while cur_line != '':
	cur_line = input_file.readline()
	# remove trailing endline
	cur_word = cur_line[:-1] 
	# if it has the same length, any key match means the word
	# 	has the same number of each letter
	if len(cur_word) == len(input) and input_key == get_key(cur_word): 
			match_list.append(cur_word) 

print "\nMatches:" 
print "\n".join(match_list)  
