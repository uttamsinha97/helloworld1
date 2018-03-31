arr=[]
print('kindly enter the number of words you want')
n=(input(n))
for x in range(1,n):
    element=input('enter word'+str(x+1))
    arr.append(element)

for x in range(1,n):
    print(arr[x])