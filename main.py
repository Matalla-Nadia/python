# def afficher_informations_personne(nom,age, taille = 0):
#     print()
#     print("Vous vous apeller" + nom + " et vous avez " + str(age) + " ans.")
#    # print(f"Vous vous apeller {nom} et vous avez {age} ans.")
#     print("L'année prochaine" + nom + " vous allez avoir " + str(age + 1) + "ans.")
#
#     # condition = age >=18
#     # print(condition)
#     # print(type(condition))
#     #if condition:
#     if age == 17:
#         print("Vous êtes presque majeur")
#     elif  12 <= age < 18:             # age >= 12 and age < 18
#         print("Vous êtes un ados")
#     elif age == 1 or age ==2:
#         print("Vous êtes un bébé")
#     elif age == 18:
#         print("Vous êtes tout juste majeur félicitation !")
#     elif age >= 60:
#         print("Vous êtes senior")
#     elif age >= 18:
#         print("Vous êtes majeur" )
#     elif age < 10:
#         print("Vous êtes enfant" )
#     else:
#         print("Vous êtes mineur")
#
#
#      # afficher la taille
#     if not taille == 0:
#         print("Votre taille est " + str(taille) + " m" )
#
#
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input( nom_personne + " quel age avez vous ?")
        try:
            age_int = int(age_str)
        except:
            print("Désolé il y'a une erreur!")
    return age_int
#
# #####Variable Globale
# # age = 0
# #
# # def demander_age():
# #     global age
# #     while age == 0:
# #         age_str = input("Quel age avez vous ? ")
# #         try:
# #             age = int(age_str)
# #         except:
# #             print("Désolé il y'a une erreur!")
#
# #######################################################
def demander_nom():
    nom_bis = ""
    while nom_bis == "" :
     nom_bis = input ("Quel est votre nom?")

    return nom_bis


# #demander nom
nom1 = demander_nom()
#nom2 = demander_nom()

# demander age
age1 = demander_age(nom1)
#age2 = demander_age(nom2)
#
#
#
# #afficher resultats
# afficher_informations_personne(nom1,age1)
# afficher_informations_personne(nom2,age2)
#
# # # boucle white : "tant que"...
# # n = 0
# # print(n)
# # n = 12
# # print(n)
# # n = n + 1
# # print(n)
# #
# # print("debut")
# # while n < 10:
# #     print("Valeur de n: " + str(n))
# #     n = n + 1
# #     print("fin")
#
# # mdp = ""
# # while not mdp == "Nadia":
# #     mdp = input("Quel est le mdp ? ")
# #
# # print("Mdp oorrect vous avez accés à votre compte")
#
# # boucle for
# NB_PERSONNES = 1  #contante en majuscule
#
# for i in range(0,NB_PERSONNES):
#     nom = "personne" + str(i+1)
#     age = demander_age(nom)
#     afficher_informations_personne(nom,age,1.75)

####################################################################################"
    # Fonction
#
# nom1 = input(" Nom de la personne 1: ")
# age1 = input("Age de la personne 1 :")
# print("La personne 1 est", nom1,"son age est", age1, "ans")
# print("Le nom comporte",len(nom1),"lettres")

# Pour eviter de dupliquer le code

#definir la fonction
def est_majeur(age):
    if age >= 18:
        return True
    return False

def afficher_infos_personne(nom, age = 0): # il ne l'execute pas, pas de return a la fin de la fonction il execute automatiquement
   if nom =="":
       print("Vous n'avez donné de nom")
       return

   if age == 0:
    print("La personne est:",nom)
   else:
    print("La personne est:", nom,",son age est", age,"ans")
    print("Le nom comporte", len(nom), "caracteres")

print("Debut")
# apel de la fonction
#afficher_infos_personne("June", 31)
age = 62

print("La personne a", age, "ans")
if est_majeur(age):
    print("Il est majeur")
else:
    print("Il est mineur")
print("est_majeur",est_majeur(62))
print("fin")

# Exercices

def afficher_table_multiplication(n, min=1, max=10):
   if min > max:
       print("Erreur : Le min est supérieur au max")
       return

   for i in range (min, max+1):
        print(i, "x" , n, "=", i*n)


afficher_table_multiplication(5, 10,1)

# exercice questionnaires

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
        global score
        print("score:", score)
        print("QUESTION")
        print(" " + question)
        print("  (a)", r1)
        print("  (b)", r2)
        print("  (c)", r3)
        print("  (d)", r4)
        print()
        reponse = input("Votre reponse : ")
        if reponse == choix_bonne_reponse:
            print("Bonne réponse")
            score += 1
        else:
            print("Mauvaise réponse")

        print()

        score = 10

poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Lisbonne", "Pékin", "Pises", "a")
print("Score final:", score)