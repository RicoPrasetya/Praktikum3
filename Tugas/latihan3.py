print("Nama : Rico Prasetya")
print("NIM  : 312210425")
print("")
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
n-=1
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()
