def szorasszamolo(ls):
    szoras = 0
    sum = 0
    db = 0
    atlag = 0
    for i in range(len(ls)):
        db += 1
        sum = sum + int(ls[i])
    try:
        atlag = int(sum/db)
    except ZeroDivisionError:
        print("A szórás nem számolható!")
    for j in range(len(ls)):
        x = (atlag - int(ls[j]))**2
        szoras += x
    try:
        return (szoras/db)**0.5
    except ZeroDivisionError:
        print("A szórás nem számolható!")
        exit(-3)

def helyiertekszamolo(ls):
    result = 0
    for i in range(len(ls)):
        firstChar = str(ls[i])[:1]
        if firstChar == "-":
            result += int(str(ls[i])[1])
        else:
            result += int(firstChar)
    return result

def tesztesetek():
    try:
        return int(input("Adjon meg egy számot:"))
    except ValueError:
        print("Számot adjon meg!")
        exit(-1)

def szamsplit():
    n2 = input("Adjon meg számokat,szóközzel elválasztva:").split(" ")
    result = []
    try:
        for i in n2:
            result.append(int(i))
        return result
    except ValueError:
        print("Számokat adjon meg egy szóközzel elválasztva!")
        exit(-2)

x = 0
n = tesztesetek()
for i in range(n):
    parosls = []
    paratlanls = []
    n2 = szamsplit()
    for j in n2:
        if j % 2 == 0:
            parosls.append(j)
        else:
            paratlanls.append(j)
    x += 1
    print("{}.sor".format(x))
    print("Páros számok szórása:","%.2f" % szorasszamolo(parosls),"Páratlan számok szórása:","%.2f" % szorasszamolo(paratlanls))
    print("Számjegyek összege(legnagyobb helyiértékek):",helyiertekszamolo(n2))