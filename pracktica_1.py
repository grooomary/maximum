def Palindrome_test_string(input_str):
    stroka = input_str
    return stroka==stroka[::-1]
print(Palindrome_test_string('приветмир'))