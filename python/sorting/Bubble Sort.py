a = []
n = int(input("Please Enter the Total Number of Elements : "))
for i in range(n):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)

for i in range(n -1):
    for j in range(n - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("The Sorted List in Ascending Order : ", a)
