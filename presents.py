x = int(input("enter number of presents: "))
n = list(map(int,input("entee the presents :").split()))
ans=[]

for j in range (1,x+1):
    for i in range (x):
        if j == n[i]:
            ans.append(i+1)

print(ans)