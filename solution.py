import math

def isPalindrome(txt):
    reversed_txt = txt[::-1]

    if reversed_txt == txt:
        print("The entered string is Palindrome")
    else:
        print("The entered string is not Palindrome")

# The given word has an Even length (Word with odd length is not going to be Symmetrical)
def isSymmetrical(txt):
    first_part_of_word = txt[:math.ceil(len(txt)/2)]
    second_part_of_word = txt[math.floor(len(txt)/2):]

    if first_part_of_word == second_part_of_word:
        print("The entered string is Symmetrical")
    else:
        print("The entered string is not Symmetrical")

mString = "amaama"
isPalindrome(mString)
isSymmetrical(mString)
