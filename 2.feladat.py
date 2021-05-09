import numpy as np

def determinansszamolo(matrix):
    if matrix.shape == (2, 2):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    determinans = 0
    for i in range(matrix.shape[1]):
        kis_matrix = np.delete(np.delete(matrix, 0, 0), i, 1)
        determinans += (matrix[0][i] * pow(-1, i)) * determinansszamolo(kis_matrix)

    return determinans

def Matrixletrehozo(a,b,x,y):
    try:
        a = int(a)
        b = int(b)
        x = int(x)
        y = int(y)
        if x != y or x == 0:
            raise ArithmeticError
        return np.random.randint(a, b, (x, y))
    except ValueError:
        print("Helytelen számot adott meg!(a legkisebb számnak kisebbnek kell lennie a legnagyobbtól)")
        exit(-1)
    except ArithmeticError:
        print("A mátrix nem hozható létre a megadott adatok alapján")
        exit(-2)

def tesztesetek():
    try:
        return int(input("Adja meg a tesztesetek számát:"))
    except ValueError:
        print("Számot adjon meg!")
        exit(-1)

fout = open("2.feladat.txt","w")
n = tesztesetek()
for i in range(n):
    a = (input("Adja meg a mátrix legkisebb számát:"))
    b = (input("Adja meg a mátrix legnagyobb számát:"))
    x = (input("Adja meg a mátrix sorainak számát:"))
    y = (input("Adja meg a mátrix oszlopainak számát:"))
    m = Matrixletrehozo(a,b,x,y)
    print(m,file=fout)
    result = determinansszamolo(m)
    print(result,file=fout)
fout.close()
