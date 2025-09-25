n=input()
a,b=0,0
k,d=-1,-1
for i in n:
    k+=1
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        a=k
        break
for i in n:
    d+=1
    if i in '0123456789':
        b=d+1
        break
print(n[a::b-a])