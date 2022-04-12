lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element

for ele in lst:
    if(lst[i]%2==0):
    print("Genap")
  else:
    print("Ganjil")