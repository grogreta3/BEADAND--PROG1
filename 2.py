def penz(d):
    szotar={'100':0,'50':0,'10':0,'5':0,'2':0,'1':0}
    while d!=0:
        n=int(input("adj meg egy szamot:"))
        while n!=0:
            if n>=100:
                n=n-100
                szotar['100']+=1
            elif n>=50 and n<100:
                n-=50
                szotar['50'] += 1
            elif n>=10 and n<50:
                n-=10
                szotar['10']+=1
            elif n>=5 and n<10:
                n-=5
                szotar['5']+=1
            elif n>=2 and n<5:
                n-=2
                szotar['2']+=1
            else:
                n-=1
                szotar['1']+=1
        d-=1
        for i in szotar:
            if szotar[i]!=0:
                print('{} db {} Ft'.format(szotar[i],i))
        szotar = {'100': 0,'50' : 0,'10':0,'5':0 ,'2':0 ,'1':0}


n=int(input("adj meg egy szamot hanyszor fusson a program:"))
print(penz(n))
