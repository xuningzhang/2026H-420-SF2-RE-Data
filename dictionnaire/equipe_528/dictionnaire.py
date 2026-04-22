class dictionnaire:
    def __init__(self):
        self.cle = []
        self.valeur = []
    
    def ajouter(self, cle, valeur):
        if cle in self.cle:
            index = self.cle.index(cle)
            self.valeur[index] = valeur
        else:
            self.cle.append(cle)
            self.valeur.append(valeur)

    def obtenir(self, cle):
        if cle in self.cle:
            index = self.cle.index(cle)
            return self.valeur[index]
        else:
            return None

    def supprimer(self, cle):
        if cle in self.cle:
            index = self.cle.index(cle)
            del self.cle[index]
            del self.valeur[index]
            return True
        else:
            return False

vehicule = dictionnaire()
vehicule.ajouter("voiture", "véhicule à quatre roues")
print(vehicule.obtenir("voiture")) 
vehicule.ajouter("vélo", "véhicule à deux roues")
print(vehicule.obtenir("vélo"))