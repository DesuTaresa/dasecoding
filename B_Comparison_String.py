n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    counter =0
    if s.count("<")==s.count(">"):
        print(s.count("<")+1)
    else:
        if m%2==0: 
            print(max(s.count("<"),s.count(">"))-1)
        else:
            print(m-2*min(s.count("<"),s.count(">"))+1)
