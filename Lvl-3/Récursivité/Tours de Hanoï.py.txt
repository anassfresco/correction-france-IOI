def deplacePile(taille, debut, fin, autre):
   if taille == 0:
      return
   deplacePile(taille - 1, debut, autre, fin)
   print("{} -> {}".format(debut, fin))
   deplacePile(taille - 1, autre, fin, debut)
taille = int(input())
deplacePile(taille, 1, 3, 2)