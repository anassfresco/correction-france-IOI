contenuTriangle = [[False] * 64 for _ in range(64)];
  
def remplitTriangle(debutX, debutY, taille):
   if taille == 1:
      contenuTriangle[debutX][debutY] = True
      return
   taille = taille // 2
   remplitTriangle(debutX, debutY, taille)
   remplitTriangle(debutX + taille, debutY, taille)
   remplitTriangle(debutX, debutY + taille, taille)
 
taille = int(input())
remplitTriangle(0, 0, taille)
for y in range(taille):
   for x in range(taille-y):
      if contenuTriangle[x][y]:
         print("#", end = "")
      else:
         print(" ", end = "")
   print()