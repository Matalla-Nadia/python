print("Bienvenue sur la calculatrice")
print("Saisir A pour l'addition")
print("Saisir S pour la soustraction")
print("Saisir M pour la multiplication")
print("Saisir D pour la division")
print("Saisir n'importe quelle valeur pour sortir du programme")

reponse = input("_")

if reponse =="A":
    a = float(input("Saisir la premiere valeur à additionner:"))
    b = float(input("Saisir la deuxieme valeur à additionner:"))
    print(a,"+",b,"=", (a+b))
elif reponse =="S":
    a = float(input("Saisir la premiere valeur pour la soustraction:"))
    b = float(input("Saisir la deuxieme valeur pour la soustraction:"))
    print(a,"-",b,"=", (a-b))
elif reponse == "M":
    a = float(input("Saisir la premiere valeur pour la multiplication:"))
    b = float(input("Saisir la deuxieme valeur pour la multiplication:"))
    print(a, "*", b, "=", (a*b))
elif reponse == "D":
    a = float(input("Saisir la premiere valeur pour la division:"))
    b = float(input("Saisir la deuxieme valeur pour la division:"))
    print(a, "/", b, "=", (a/b))
else:
    print("Au revoir")