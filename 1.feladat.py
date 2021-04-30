def szorasszamolo(ls):
    szoras = 0
    sum = 0
    db = 0
    for i in range(len(ls)):
        db += 1
        sum = sum + int(ls[i])
    atlag = int(sum/db)
    for j in range(len(ls)):
        x = (atlag - int(ls[j]))**2
        szoras += x
    result = (szoras/db)**0.5
    return result


def helyiertekszamolo(ls):
    result = 0
    for i in range(len(ls)):
        firstChar = str(ls[i])[:1]
        if firstChar == "-":
            result += int(str(ls[i][1]))
        else:
            result += int(firstChar)
    return result

x = 0
n = int(input("Adjon meg egy számot:"))
for i in range(n):
    parosls = []
    paratlanls = []
    n2 = input("Adjon meg számokat,szóközzel elválasztva:").split(" ")
    for j in range(len(n2)):
        if int(n2[j]) % 2 == 0:
            parosls.append(n2[j])
        else:
            paratlanls.append(n2[j])
    x += 1
    print("{}.sor".format(x))
    print("Páros számok szórása:",szorasszamolo(parosls),"Páratlan számok szórása:",szorasszamolo(paratlanls))
    print("Számjegyek összege(legnagyobb helyiértékek):",helyiertekszamolo(n2))




