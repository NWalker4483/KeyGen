def xyz(y):
    thefile = open('test.xyz', 'w')
    itemlist=y
    lis=[]
    #thefile.write(str(len(y))+"\n")
    #thefile.write("New Trial"+"\n")
    for i in itemlist:
        b=""
        for a in i:
            b+=str(a)[:8].ljust(8,"0").ljust(12)
        '''
        for c in i:
            b+=str(int(255*c)%255).ljust(5," ")
        '''
        lis.append(b)
    thefile.write("\n".join(lis))
import numpy as np
X = np.arange(0, 40, 0.25)
Y = np.arange(0, 40, 0.25)
X, Y = np.meshgrid(X, Y)
C=[list(zip(X[i],Y[i],X[i]-Y[i])) for i in range(len(X))]
C=sum(C,[])
#Z = np.sin(X)*np.sin(Y)
xyz(C)

