# -*- coding: utf-8 -*-

# Q1
def callnum(digits):
    callnumbers = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    output = [key for key in callnumbers[digits[0]]]
    print(output)
    for index in range(1, len(digits)):
        number = digits[index]
        if number in [0, 1]:
            break
        options = []
        for key in callnumbers[number]:
            options += [option + key for option in output]
            print(options)
        output = options
    return output


callnum(['3', '5'])

# Q2
def changeNumToChar(self, toSmallChar=None, toBigChar=None):
    init_number = 0
    increment = 0
    res_char = ''
    if not toSmallChar and not toBigChar:
        return ''
    else:
        if toSmallChar:
            init_number = toSmallChar
            increment = ord('a') - 1
        else:
            init_number = toBigChar
            increment = ord('A') - 1

    shang, yu = divmod(init_number, 26)
    char = chr(yu + increment)
    res_char = char * (shang + 1)
    print(res_char)
    return res_char

changeNumToChar(0,8)