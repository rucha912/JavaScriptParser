'''

Created by Rucha Kadam

The following code is used for reporting the following from a Javascript file:

1. undeclared variables in a code
2. oneline if..else statements
3. undeclared functions
4. unbalanced paranthesis in the code

'''
import sys
import re

def extract_variables(filename):
	f = open(filename, 'r')
        print "\nUNDECLARED VARIABLES:\n"
        var_list = []

        #take the whole line with the word let or var in it
        for line_number, line in enumerate(f):
            var = re.findall('(let|var)(.*)\s*=*\s*(?=;)', line)
            if len(var)>0:
                var_list.append((var[0], line_number + 1))


#make a list with just variable names and their line number
        for place, item in enumerate(var_list):
            junk , var = item[0]

            temp =  var.split('=')
            new_key = temp[0].strip()
            var_list[place] = (new_key, item[1])

#make a new dictionary to count the occurrence of the variables
        new_dict = {}
        for item in var_list:
            new_dict[item] = 0

#instantiate file iterator again
        f = open(filename, 'r')

#count occurrence of variable and store it in dictionary
        for line in f:
            for key in new_dict.iterkeys():
                if line.strip().startswith('//'):
                    pass
                else:   
                    pattern = '\\b' + key[0] + '\\b'
                    find = re.search(pattern, line)
                    if find!=None:
                        new_dict[key] = new_dict[key] + 1

#Print variables with only one occurrence as unused 
        for key, value in  new_dict.iteritems():
            if value == 1:
                print "Unused Variable -> ", key[0], "at line:", key[1]
        
def extract_conditionals(filename):
        f = open(filename, 'r')
        i = 1
        print '\nONELINE IF..ELSE STATEMENTS:\n'
        #iterate the file while keeping track of line number
        for line_number, line in enumerate(f):
            line_num = line_number + i
            #find lines that have if statements
            if line.startswith('if') and '{' not in line:
                if next(f).startswith('{') == False:           
                    print "IF statement found at:", line_num, "\n->", line
                    i = i + 1
                else:
                    i = i + 1
            #find lines that have else statements
            if line.startswith('else') and '{' not in line:
                if next(f).startswith('{') == False:           
                    print "ELSE statement found at:", line_num, "\n->", line
                    i = i + 1
                else:
                    i = i + 1

def balance_paranthesis(filename):
        f = open(filename,'r')
        print "\nUNBALANCED PARANTHESIS:\n"
        #instatiate a counter to keep track of paranthesis
        count = 0
        for line_number, line in enumerate(f):
                if '{' in line:
                        count = count + 1
                if '}' in line:
                        count = count - 1
                        
        #if count is 0, opening brackets match closing, hence it's balanced
        if count == 0:
                print 'The paranthesis are balanced in your code\n'
        if count < 0:
                print 'There is an extra paranthesis in your code\n'
        if count > 0:
                print 'There is a missing paranthesis in your code\n'

def extract_functions(filename):

        f = open(filename, 'r')
        print "\nUNDEFINED FUNCTIONS:\n"
        pattern_list = []

        #find lines having "()" pattern in them
        for line_number, line in enumerate(f):
            pattern = re.search('(.*\s*\(.*\))', line)
            if pattern:
                pattern_list.append((pattern.group(), line_number))

	#create a new list which doesn't have "if", "set" or "console" in them
        new_list = []
        for item in pattern_list:
            pattern, line_number = item
            if 'console' not in pattern and 'if' not in pattern and 'constructor' not in pattern and 'set' not in pattern and 'new' not in pattern:
                new_list.append(item)

        #extract the functions that were declared and that were used from the list
        declared_function = []
        used_function = []
        for item in new_list:
            dec_funct, line_number = item
            if 'function' in dec_funct:
                declared_function.append(item)
            else:
                used_function.append(item)

        #if the name appears in used_function but not in used_function, report it as undeclared
        flag = 0
        for u_funct in used_function:
            u_name, u_num = u_funct
            for d_funct in declared_function:
                d_name, d_num = d_funct
                e_pat = "\\b" + u_name.strip('()') + "\\b"
                exact = re.search(e_pat, d_name)
                if exact:
                    flag = 1
            if flag != 1:
                print "Undefined function -> ", u_name , "found at", u_num
        
def main():
    filename = sys.argv[1]
    print 'Hi there! Here\'s your javascript file parser implemented in PYTHON.\n'
    extract_variables(filename)
    extract_conditionals(filename)
    balance_paranthesis(filename) 
    extract_functions(filename)
    
if __name__ == '__main__':
  main()
