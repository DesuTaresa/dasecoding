n, k, l, c, d, p, nl, np=map(int,input().split())
s=(k*l)//nl
h=c*d
d=p//np
print(min(s,h,d)//n)
