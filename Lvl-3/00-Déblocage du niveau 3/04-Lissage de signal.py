import math


def testEcart(listeTest, diffMax, nbValeurs):
    for i in range(nbValeurs - 1):
        diff = listeTest[i] - listeTest[i + 1]
        if abs(diff) >= diffMax:
            return False
    return True


nbMesures = int(input())
diffMax = float(input())

listeMesures = [float(input()) for i in range(nbMesures)]
listeInt = listeMesures[:]

comptePassages = 0

while not testEcart(listeMesures, diffMax, nbMesures):
    for id in range(1, nbMesures - 1):
        listeInt[id] = round(((listeMesures[id - 1] + listeMesures[id + 1]) / 2), 5)
    listeMesures = listeInt[:]
    comptePassages += 1

print(comptePassages)
