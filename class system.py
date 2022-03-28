"""La programation orienté objet avec le language python """

"""Classe : plan de conception, genre (ex : humain )"""
"Objet  : instance d'une classe (ex : Julien , est un objet de classe Humain)"
""" Atribut :variable de classe (ex : prenom , age , taille , sexe)"""
""" Ce n'est qu'une exemple afin de m aider à me rappeller des classes , objet et attribut dans le code """
class Voiture:
    """
    Classe des voitures
    """
    nbr_voiture = 0
    def __init__(self,types,carbone,vitesse):
        print("Création d'une voiture...")
        self.types = types
        self.construction = carbone
        self.speed = vitesse 
        Voiture.nbr_voiture += 1
    def spawn(types,carbone,vitesse,nbr):
        system=[]
        for i in range(nbr):
            #peut installer un choix de type aléatoire  
            system.append("voiture"+str(i+1))
            system[i]= Voiture(types,carbone,vitesse)
        return system
            
        
    
print("Lancement du programme ...")

v1 = Voiture("Thermique",2400,130)
print("le type de voiture de v1 est {}".format(v1.types))
print("Le coût cabonne de la construction de v1 est {}".format(v1.construction))
v2 = Voiture("Electrique",6350,150)
print("v2 est de type {}".format(v2.types))
print("Le coût cabonne de la construction de v2 est {}".format(v2.construction))
v=Voiture.spawn("Thermique",2400,130,5)
print(format(v[1].types))
