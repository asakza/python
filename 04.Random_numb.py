#### Assignment : Print 100 random numbers and save them in a list

import random
strt_num = 1
end_num = 100
max_len = 100
my_lit = []
for var1 in range(max_len+1):
    my_lit.append(random.randint(strt_num,end_num))

#### Printing numbers if value is greater than 40
for var2 in range(max_len):
    if (my_lit[var2]) > 40:
        print(my_lit[var2])

#### Sum of number is list
lst_sum = sum(my_lit)
print(lst_sum)

#### Minimum value in list
mnm_lst = min(my_lit)
print(mnm_lst)

#### Maximum value in list
mxm_lst = max(my_lit)
print(mxm_lst)