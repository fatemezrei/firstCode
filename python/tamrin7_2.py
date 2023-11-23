def find(a, n):
    notMach = True
    for i in range(n):
        for j in range(i+1, n):

            if a[i] + a[j] in a:
                notMach = False
                print(a[i], a[j])
                break

    if notMach == True:
        print('not exist')    


n = int(input())
a = []
for i in range(n):
    element = int(input())
    a.append(element)
    
find(a, n)





