y = int(input)
a = 1
b = 1
n = 0
hasil = 0
while True:
    if n < y:
        print(a)
        n = n + 1
        a = a + 1
        hasil = hasil + a
    else:
        break
        
print("Sn = {}".format(hasil))