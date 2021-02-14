def main():
   nbLignes, nbColonnes = map(int, input().split())
   image = [["."] * nbColonnes for _ in range(nbLignes)]
   nbRectangles = int(input())
   for iRectangle in range(nbRectangles):
      donnéesRect = input().split()
      iLig1, iCol1, iLig2, iCol2 = map(int, donnéesRect[:4])
      couleur = donnéesRect[4]
      for  iLig in range(iLig1, iLig2 + 1):
         for iCol in range(iCol1, iCol2 + 1):
            image[iLig][iCol] = couleur
   for ligne in image:
      print("".join(ligne))
main()