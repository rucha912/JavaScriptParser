import sys
import re

def extract_variables(filename):
	variables = []          #store all variables in a list
	occurences = []         #store the number of occurences of a particular variable
	matches = []            #store the final list of variables in a list
	f1 = open(filename, 'rU')
	text = f1.read()
	f1.close()
	f2 = open(filename, 'r')
	lines = f2.readlines()
	#print lines
	line_no = 0
	matches = re.findall('var\s+([a-zA-Z_][a-zA-Z0-9_]{0,31})', text)
	for match in matches:
                occurences = re.findall(match, text)
                if len(occurences) == 1:
                        variables.append(match)        
        print '\nHere are variables that were declared but never used:\n'
        for variable in variables:
                print 'name of the variable:', variable
                for (num, line) in enumerate(lines, 1):
                        if variable in line:
                                print 'found at line:', num , '\n'
        f2.close()

def extract_conditionals(filename):
        f = open(filename, 'r')
        i = 1
        print '\nHere are one line if..else statements:\n'
        for line_number, line in enumerate(f):
            line_num = line_number + i
            if line.startswith('if') and '{' not in line:
                if next(f).startswith('{') == False:           
                    print "IF statement found at:", line_num, "\n->", line
                    i = i + 1
                else:
                    i = i + 1

            if line.startswith('else') and '{' not in line:
                if next(f).startswith('{') == False:           
                    print "ELSE statement found at:", line_num, "\n->", line
                    i = i + 1
                else:
                    i = i + 1

def balance_paranthesis(filename):
        f = open(filename,'r')
        count = 0
        for line_number, line in enumerate(f):
                if '{' in line:
                        count = count +1
                if '}' in line:
                        count = count - 1

        if count == 0:
                print 'The paranthesis are balanced in your code'
        if count < 0:
                print 'There is an extra paranthesis in your code'
        if count > 0:
                print 'There is a missing paranthesis in your code'

def main():
    filename = sys.argv[1]
    print 'Hi there! Here\'s your javascript file parser implemented in PYTHON.\n'
    extract_variables(filename)
    extract_conditionals(filename)
    balance_paranthesis(filename) 

if __name__ == '__main__':
  main()
