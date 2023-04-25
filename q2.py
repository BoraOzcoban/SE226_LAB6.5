str_list = ['racecar', 'level', 'hello', 'world', 'deified']

def palindrome_strings(str_list):
    palindrome_list = []
    for string in str_list:
        if string == string[::-1]:
            palindrome_list.append(string)
    return palindrome_list

palindrome_list = palindrome_strings(str_list)
print(palindrome_list)
