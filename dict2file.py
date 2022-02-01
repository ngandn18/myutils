import ast
# with open('logs.txt', 'r') as f:
# #     line = f.readline()
#     x = ast.literal_eval(f.readline())
#     print(type(x),'\n', x.keys())

# filename = 'a.txt'
# my_dict = x
# with open(filename, 'w') as f:
#     f.write(str(my_dict))

def dict_2_file(dic, filename):
    '''
    dic: dictionary saved to filename
    '''
    with open(filename, 'w') as f:
        f.write(str(dic))

# dict_2_file(mydict, 'a.txt')

def dict_fr_file(filename):
    '''
    filename: file loaded to dic
    '''
    # import ast
    with open(filename, 'r') as f:
        return ast.literal_eval(f.readline())

# Testing
# mydict = dict_fr_file('logs.txt')
# dict_2_file(mydict, 'a.txt')
# print(mydict)