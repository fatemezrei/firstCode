def find(a, n):
    for i in range(n):
        for j in range(i+1, n):

            if a[i] + a[j] in a:
                print(a[i], a[j])
                break

            else:
                print('not exist')    


n = int(input())
a = []
for i in range(n):
    element = int(input())
    a.append(element)
    
find(a, n)





