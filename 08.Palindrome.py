from sqlalchemy import null
wrd_input= input("Please Enter any word ")
entr_wrd = wrd_input.upper()
vartype=null
if len(entr_wrd)%2==0:
    vartype="Even"
else:
    vartype="odd"

###Mid-point for Odd number
st_a = (len(entr_wrd)-1)  ## Divided in 2 sets (Exmple 11-1)
mid_num_odd = int((st_a/2)+1) ## Added +1 for mid point list (5+1 : which means 6 is mid for 11)
print(mid_num_odd)

### Mid-point for Even number
mid_num_even = int(len(entr_wrd)/2)

if vartype=="odd":
    for i in range((mid_num_odd)-1):
        var1=(entr_wrd[i])
        var2=(entr_wrd[(i+1)*-1])
        print(var1,var2)
    if var1==var2:
        print("Entered word is a Palindrome")
    else: 
        print("Entered word in not a Palindrome")
if vartype=="Even":
    for i in range((mid_num_even)):
        var1=(entr_wrd[i])
        var2=(entr_wrd[(i+1)*-1])
        print(var1,var2)
    if var1==var2:
        print("Entered word is a Palindrome")
    else:
        print("Entered word in not a Palindrome")