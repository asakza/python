entrd_word = input("Please Enter any Word ")
n_lst =[]
for chr in range(len(entrd_word)):
    print(chr,entrd_word[chr])
    n_lst.append(entrd_word[chr])

for chr2 in range (len(entrd_word)):
    print(f"The Character {n_lst[chr2]} is appearing",n_lst.count((entrd_word[chr2])))
