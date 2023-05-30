Tab = [18,47,8,21,34]
for n in range (1,n):
    j=i
    memoire=Tab[i]

while(j>0) and memoire<Tab[j-1]:
    Tab[j-1],Tabl[j] = Tab[j],Tab[j-1]
    j = j - 1

Tab[j]= memoire