import sys
import re

def extract_variables(filename):
	f = open(filename, 'r')

        var_list = []

        #take the whole line with the word let or var in it
        for line_number, line in enumerate(f):
            var = re.findall('(let|var)(.*)\s*=*\s*(?=;)', line)
            if len(var)>0:
                var_list.append((var[0], line_number + 1))

#print var_list

#make a list with just variable names and their line number
        for place, item in enumerate(var_list):
            junk , var = item[0]

            temp =  var.split('=')
            new_key = temp[0].strip()
            var_list[place] = (new_key, item[1])

#print var_list

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
                print "Unused Variable: ", key[0], "at line:", key[1]
        
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
        count1 = 0
        count2 = 0
        count = 0
        for line_number, line in enumerate(f):
                if '{' in line:
                        count1 = count1 + 1
                        count = count + 1
                if '}' in line:
                        count2 = count2 + 1
                        count = count - 1

        if count1 == 0:
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
