import ast
import json

def dict_2_file(dic, filename):
    '''
    dic: dictionary saved to filename by "str(dictionary)"
    '''
    with open(filename, 'w') as f:
        f.write(str(dic))

# dict_2_file(mydict, 'a.txt')

def dict_fr_file(filename):
    '''
    filename: file loaded to dic
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read().replace("'",'"'))
    # import ast
    # with open(filename, 'r') as f:
    #     return ast.literal_eval(f.readline())

# Testing
# mydict = dict_fr_file('logs.txt')
# dict_2_file(mydict, 'b.txt')
# print(mydict.keys())

# with open('a.txt', 'r') as f:
#     line = f.read()
# # line = line.replace("'", '"')
# dict=json.loads(line.replace("'", '"'))
# print(type(line),'\n', line)
# dict.keys()