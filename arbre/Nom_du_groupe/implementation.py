class Binary_nodes:
    def __init__(self, valeur: float, fils_gauche, fils_droit):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit

    def check_for_children(self):
        if self.fils_gauche == None and self.fils_droit == None:
            return "empty"
        elif self.fils_gauche == None or self.fils_droit == None:
            if self.fils_gauche == None:
                return "gauche"
            else:
                return "droit"
        else:
            return False




class Binary_tree:
    def __init__(self, racine: Binary_nodes):
        self.racine = racine
    
    def add_node(self, ajout:Binary_nodes, parent: Binary_nodes):
        pass
         
    def remove_node(self):
        pass
    
    def hauteur(self):
        pass
    
    def search(self, clef: Binary_nodes.valeur):
        index = None
        current_node = self.racine
        while index == None:
            if clef < current_node.valeur:
                if current_node.check_for_children() == "gauche":
                    current_node = current_node.fils_gauche
            
        
    
    def afficher(self):
        pass
    
    def number_of_nodes(self):
        pass