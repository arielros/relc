#testing asaf
import os

def append_function(file, name, parameters, body):
    
    header = "def " + name + "(" + parameters + "):\n"
    file.write(header)
    lines = body.splitlines(True)
    for line in lines:
        file.write("\t" + line)
    file.write("\n")



code = '''print("first line of code")\nprint("second line of code")\n'''
filename = 'output/impl.py'
ops = {"empty": "",          \
       "insert": "r, t",     \
       "remove": "r, s",     \
       "update": "r, s, u",  \
       "query": "r, s, C"}

# create dir if it doesnt exist
d = os.path.dirname(filename)
if not os.path.exists(d):
    os.makedirs(d)
    
file = open(filename, 'a')

for op in ops:
    append_function(file, op, ops[op], code)

file.close()

compTree = dict()
