def penz(d):
    szotar={'100Ft':0,'50Ft':0,'10Ft':0,'5Ft':0,'2Ft':0,'1Ft':0}
    while d!=0:
        n=int(input("adj meg egy szamot:"))
        while n!=0:
            if n>=100:
                n=n-100
                szotar['100Ft']+=1
            elif n>=50 and n<100:
                n-=50
                szotar['50Ft'] += 1
            elif n>=10 and n<50:
                n-=10
                szotar['10Ft']+=1
            elif n>=5 and n<10:
                n-=5
                szotar['5Ft']+=1
            elif n>=2 and n<5:
                n-=2
                szotar['2Ft']+=1
            else:
                n-=1
                szotar['1Ft']+=1
        d-=1
        print(szotar)
        szotar = {'100Ft': 0,'50Ft' : 0,'10Ft':0,'5Ft':0 ,'2Ft':0 ,'1Ft':0}


n=int(input("adj meg egy szamot hanyszor fusson a program:"))
print(penz(n))
