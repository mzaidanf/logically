lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
    
print(lst)    

def dup(lst):
    lst = set()
    for ele in lst:
        if ele in lst:
            return True
        else:
            lst.add(ele)         
    return False

result = dup(lst)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')    