n =[1,2,1 ,3,3,4,5,5]
freq ={}
for x in n:
    freq[x]=freq.get(x,0)+1

print(freq)