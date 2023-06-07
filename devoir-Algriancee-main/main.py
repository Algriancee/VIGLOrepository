from fastapi import FastAPI 




app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Bienvenue sur l'application /category pour acceder a la liste des categorie   /owner pour acceder liste des engins /bills au facture  "}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}





# Endpoint pour la catégorie d'engin
#@app.route('/category/<category>')
#sync def Liste_Categorie(categorie):
   
   # Engins = []

    #return {"message": f"Hello liste des engins {Engins}"}




@app.get("/category/{category}")
def get_engins_by_category(category: str):
    # Logique pour obtenir la liste des engins de la catégorie spécifiée
    engins = []  # Liste vide dans cet exemple

    return {"category": category, "engins": engins}




# Exemple de données d'engins et de propriétaires
engins_data = [
    {"id": 1, "name": "Engin 1", "owner": "Propriétaire 1"},
    {"id": 2, "name": "Engin 2", "owner": "Propriétaire 2"},
    {"id": 3, "name": "Engin 3", "owner": "Propriétaire 1"},
    {"id": 4, "name": "Engin 4", "owner": "Propriétaire 3"},
]

@app.get("/owner/{owner}")
def get_engins_by_owner(owner: str):
    engins = [engin for engin in engins_data if engin["owner"] == owner]
    return {"owner": owner, "engins": engins}






# Exemple de données d'engins et de factures
engins_data = [
    {"immatriculation": "ABC123", "owner": "Propriétaire 1"},
    {"immatriculation": "DEF456", "owner": "Propriétaire 2"},
    {"immatriculation": "GHI789", "owner": "Propriétaire 1"},
    {"immatriculation": "JKL012", "owner": "Propriétaire 3"},
]

bills_data = [
    {"immatriculation": "ABC123", "amount": 100},
    {"immatriculation": "GHI789", "amount": 200},
]

@app.get("/bills/{owner}")
def get_bills_by_owner(owner: str):
    owner_engins = [engin["immatriculation"] for engin in engins_data if engin["owner"] == owner]
    owner_bills = [bill for bill in bills_data if bill["immatriculation"] in owner_engins]
    
    total_amount = sum(bill["amount"] for bill in owner_bills)
    
    return {"owner": owner, "bills": owner_bills, "total_amount": total_amount}


