import json



contacts = []


def ajouter_Contact(nom, prenom, telephone,email):
	contacts.append({"Nom": nom, "Prenom" : prenom, "Telephone" : telephone,"Email" : email})


def afficher_Contact():
	if not contacts:
		print("Le contact est vide. \n")
	else:
		for i in contacts:
			print(f"Nome : {i['Nom']} - Prenom : {i['Prenom']} - Telephone : {i['Telephone']} - Email : {i['Email']}")


def Chercher_Nom(nom):
	b = False
	if not contacts:
		print("Le contact est vide. \n")
	else:
		for i in contacts:
			if i['Nom'].lower() == nom.lower():
				b = True
				print(f"Nome : {i['Nom']} - Prenom : {i['Prenom']} - Telephone : {i['Telephone']} - Email : {i['Email']}")
	if b == False:
		print("Le nom n'existe pas dans le contact. \n")



def Supprimer_Contact(nom, prenom):
	b = False
	if not contacts:
		print("Le contact est vide. \n")
	else:
		for i in contacts:
			if i['Nom'].lower() == nom.lower() and i['Prenom'].lower() == prenom.lower():
				b = True
				contacts.remove(i)

	if(b == False):
		print("Le nom n'existe pas dans le contact. \n")
	else:
		print("Le contact a ete supprimer. \n")


def sauvgarder(fichier="contacts.json"):
	try:
		with open(fichier, "a") as f: 
                	json.dump(contacts, f)
		print("Le contact a ete sauvgarder. \n")
	except:
		print("Error, dans la creation de fichier. \n")

def charger(fichier="contacts.json"):
	global contacts
	try:
		with open(fichier, "r") as f:
			contacts = json.load(f)
		print("Le contact a ete charge. \n")
	except FileNotFoundError:
		print("Error, aucun fichier trouve.\n")
	except json.JSONDecodeError:
        	print("Erreur : fichier vide ou corrompu.\n")

def menu():
	while True:
		print("******************************************************************************************************** \n")
		print("Taper \"1\" pour ajouter un contact.\n")
		print("Taper \"2\" pour afficher les contacts.\n")
		print("Taper \"3\" pour chercher un nom. \n")
		print("Taper \"4\" pour supprimer un contact. \n")
		print("Taper \"5\" pour sauvgarder les contacts. \n")
		print("Taper \"6\" pour charger les contacts. \n")
		print("Taper \"0\" pour quiter.\n")
		print("******************************************************************************************************** \n")


		choix = input("Taper le choix ici : ")
		print("\n")
		if choix == "1":
			nom = input("Taper le nom : ")
			prenom = input("Taper le prenom : ")
			telephone = input("Taper le numero de telephone : ")
			email = input("Taper l'email : ")
			ajouter_Contact(nom, prenom, telephone, email)
		elif choix == "2":
			afficher_Contact()

		elif choix == "3":
			nom = input("Taper le nom : ")
			Chercher_Nom(nom)
		elif choix == "4":
			nom = input("Taper le nom : ")
			prenom = input("Taper le prenom : ")
			Supprimer_Contact(nom, prenom)
		elif choix == "5":
			sauvgarder()

		elif choix == "6":

			charger()
		elif choix == "0":
			break
		else:
			print("Taper un choix entre 0 et 6. \n")





menu()
