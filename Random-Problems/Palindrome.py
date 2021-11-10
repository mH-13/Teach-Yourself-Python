#string reverse
def check_Palindrome(strng):
    strng1 = ''
    strng2 = ''
    for i in strng:
        if i == ' ':
            strng1 += i
        else:
            strng2 += i

    new_strng = ''
    new_strng = strng2[-1::-1]

    if new_strng == strng2:
        print("This is a palindrome")
    else:
        print('This is not a palindrome')


check_Palindrome(input("enter a string: "))
