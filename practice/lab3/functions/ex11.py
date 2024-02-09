def check_palindrome(s):
    bool = True
    for i in range(len(s)/2):
        if(s[i] != s[len(s) - 1 - i]):
            bool = False
            break
    return bool
print(check_palindrome)