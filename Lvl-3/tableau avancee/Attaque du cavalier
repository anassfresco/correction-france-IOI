def main():
   echiquier = [input() for loop in range(8)]
   
   def piece(ligne,colonne):
      if (ligne < 0) or (ligne >= 8) or (colonne < 0) or (colonne >= 8):
         return ' '
      return echiquier[ligne][colonne]
   
   mouvements = [(+1,+2),(+1,-2),(-1,+2),(-1,-2),(+2,+1),(+2,-1),(-2,+1),(-2,-1)]
   
   def attaqueDeCavalier():
      for ligne in range(8):
         for colonne in range(8):
            if echiquier[ligne][colonne] == 'C':
               for ( deltaLigne, deltaColonne ) in mouvements:
                  if piece(ligne + deltaLigne, colonne + deltaColonne).islower():
                     return True
      return False
      
   if attaqueDeCavalier():
      print("yes")
   else:
      print("no")
main()
