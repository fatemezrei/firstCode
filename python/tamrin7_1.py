n, m = input().split(',')
n = int(n)
m = int(m)
a = []
while n > 0:
    a.append(input())
    n -= 1

b = []
for i in range(m):
    x = input()
    b.append(x)

# b = []
# while m > 0:
#     b.append(input())
#     m -= 1

def equal(a):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == b[j]):
                c.append(a[i])
    print(c)            
                

equal(a)


print(a)
print(b)