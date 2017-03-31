import sys
import re

def extract_variables(filename):
	variables = []
	usage = []
	matches = []
	f = open(filename, 'rU')
	text = f.read()
	variables = re.findall('var\s+([a-zA-Z_][a-zA-Z0-9_]{0,31})', text)
	for variable in variables:
                usage = re.findall(variable, text)
                if len(usage) == 1:
                        matches.append(variable)
        print '\nHere are variables that were declared but never used:'
        for match in matches:
                print match

def main():
    filename = sys.argv[1]
    print 'Hi there! Here\'s your javascript file parser implemented in PYTHON.\n'
    variables = extract_variables(filename)

if __name__ == '__main__':
  main()
