import numpy as np

def determinans(m):
    det = 0
    print(m.shape)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            det += m[j][i] * -1**(i+j)

    return det


fout = open("2.feladat.txt","w")
n = int(input("Adja meg a tesztesetek számát:"))
for i in range(n):
    a = int(input("Adja meg a mátrix legkisebb számát: "))
    b = int(input("Adja meg a mátrix legnagyobb számát: "))
    x = int(input("Adja meg a mátrix sorainak számát:"))
    y = int(input("Adja meg a mátrix oszlopainak számát:"))
    m=np.random.randint(a,b,(x,y))
    print(m,file=fout)
    result = determinans(m)
    print(result,file=fout)

