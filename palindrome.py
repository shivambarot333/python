lst = ['madam', 'python', 'malayalam',12312]

def ispalindrome (s):
    s=str(s)
    return True if s==s [::-1] else False

## for x in lst :
## print(x, ispalindrome(x))


##palindrome_list = list(filter(ispalindrome,lst))
##print(lst, palindrome_list)


palindrome_list = list(filter(lambda s : str(s) [::-1],lst))
print(lst, palindrome_list)
