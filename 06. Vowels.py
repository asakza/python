letter = input("Please Enter letter")
l2 = letter.upper()
vowels = ["A" , "E" , "I", "O", "U"]
for ltr in range(len(vowels)):
    if vowels[ltr] == l2:
        print("Entered Character is a Vowel")
        break
    if ltr == (len(vowels)-1):
        print("Entered Charcter is Consonent")    