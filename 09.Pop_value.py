lst_rng = 7
n_lst=[]
### Creating a new list with 7 integers
for var_i in range(lst_rng+1):
    n_lst.append(var_i)
print(n_lst)

### Removing integers one by one from list
for var_j in range(len(n_lst)):
    n_lst.pop()
#### This will print and show instance every time a list is popped
    print(n_lst)

print(n_lst)
