def szorasszamolo(ls):
    szoras = 0
    sum = 0
    db = 0
    for i in range(len(ls)):
        db += 1
        sum += i
    atlag = sum / db
    for j in range(len(ls)):
        x = (atlag - j)**2
        szoras += x
    result = (szoras/db)**0,5
    return result

n = int(input("Adjon meg egy számot:"))
parosls = []
paratlanls = []
for i in range(n):
    n2 = input("Adjon meg számokat,szóközzel elválasztva:")
    reszek = n2.split(" ")
    for j in range(len(reszek)):
        if j % 2 == 0:
            parosls.append(j)
        else:
            paratlanls.append(j)




