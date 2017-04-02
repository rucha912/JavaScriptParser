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

def main():
    filename = sys.argv[1]
    print 'Hi there! Here\'s your javascript file parser implemented in PYTHON.\n'
    variables = extract_variables(filename)
    #conditionals = extract_conditionals(filename)

if __name__ == '__main__':
  main()
