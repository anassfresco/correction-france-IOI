def main():
   taille = int(input())
   plateau = [list(map( int, input().split() )) for loop in range(taille)]
   
   def pion(ligne,colonne):
      nonlocal taille
      if (ligne < 0) or (taille <= ligne) or (colonne < 0) or (taille <= colonne):
         return 0
      else:
         return plateau[ligne][colonne]
   
   deltaLig = [-1,0,1,1]
   deltaCol = [1,1,1,0]
   
   for ligne in range(taille):
      for colonne in range(taille):
         joueur = plateau[ligne][colonne]
         if joueur > 0:
            for direction in range(4):
               lig = ligne
               col = colonne
               alignés = 1
               for loop in range(4):
                  lig += deltaLig[direction]
                  col += deltaCol[direction]
                  if pion(lig,col) == joueur:
                     alignés += 1
               if alignés == 5:
                  print(joueur)
                  exit(0)
   print(0)
   
main()
