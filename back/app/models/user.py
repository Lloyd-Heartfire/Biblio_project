# On importe les types nécessaires pour définir les colonnes
from sqlalchemy import Column, Integer, String, Text

# On importe la classe de base qui sert de modèle commun
from .base import Base

# On crée le modèle User qui représente la table "users" dans la base avec :
class User(Base):

    ## ID de l'utilisateur, obligatoire, avec un index pour les recherches
    id = Column ("id_user", Integer, primary_key= True, index=True)

    ## Pseudonyme de l'utilisateur
    username = Column(String(255), nullable=False, index=True)

    ## Email de l'utilisateur, facultatif
    email = Column(String(255), nullable=False)

    ## Mot de passe de l'utilisateur
    password = Column(Text, nullable=False)

    ## Rôle de l'utilisateur sur l'appli
    role = Column(String(255), nullable=False)