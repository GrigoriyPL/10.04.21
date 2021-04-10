input_string = input()
def check_string_brackets(input_string):
    if (input_string.count('(') == input_string.count(')')) or input_string =='':
        print('yes')
    else: print('No')
check_string_brackets(input_string)
