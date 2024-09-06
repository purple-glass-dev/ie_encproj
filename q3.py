#Uses a function to determine if a given string is a palindrome.
#In the main function, swaps the case of all letters in the original string 
# (e.g., Input: aBC, Output: Abc).
ms=''
def palindrome(s):
    if s == s[:-1]:
        print(s,"is a palindrome")
    else:
        print(s,"is NOT a palindrome")
s=input("Enter the string:")
palindrome(s) #Calling the function
print("String before exchange :",s)
#Exchange happens
for i in range(len(s)):
    if s[i].isupper():
        ms+=s[i].lower()
    elif s[i].islower():
        ms+=s[i].upper()
    else:
        continue 
print("String after exchange :",ms)