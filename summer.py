n = int(input("enter days: "))
f = int(input("enter days taken: "))

price=[]
ref=[]
a=[]
b=[]
ans=0

for i in range(n):
    k,l = map(int,input("enter stock and customers: ").split())
    price.append(k-l)
    ref.append(k-l)
    a.append(k)
    b.append(l)
ref.sort()

for i in range(f):
        x=price.index(ref[i])
        y=a[x]
        a[x] = y*2
        
for i in range (n):
      if a[i] >b[i]:
            ans=ans+b[i]
      elif a[i]<b[i]:
            ans=ans+a[i]
      elif a[i]==b[i]:
            ans=ans+a[i]

print(ans)




