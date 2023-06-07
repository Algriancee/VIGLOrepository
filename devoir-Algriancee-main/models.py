from fastapi import FastAPI 
from pydantic import BaseModel




app = FastAPI()

class Engins(BaseModel):
    id_engins:int
    Proprietaire:str
    Categorie:str

class Categories(BaseModel):
    id_categorie:int
    Engin:Engins
    nom_categorie:str

class Proprietaire(BaseModel):
    id_Proprietaire:int
    nbr_Engins:int
    Cotation_assurance:int
    Majoration_economat:int
    Montant_total_facture:int
    Facture:int
    Reglements:str


