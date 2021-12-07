def afficher_informations_personne(nom,age, taille = 0):
    print()
    print("Vous vous apeller" + nom + " et vous avez " + str(age) + " ans.")
   # print(f"Vous vous apeller {nom} et vous avez {age} ans.")
    print("L'année prochaine" + nom + " vous allez avoir " + str(age + 1) + "ans.")

    # condition = age >=18
    # print(condition)
    # print(type(condition))
    #if condition:
    if age == 17:
        print("Vous êtes presque majeur")
    elif  12 <= age < 18:             # age >= 12 and age < 18
        print("Vous êtes un ados")
    elif age == 1 or age ==2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Vous êtes tout juste majeur félicitation !")
    elif age >= 60:
        print("Vous êtes senior")
    elif age >= 18:
        print("Vous êtes majeur" )
    elif age < 10:
        print("Vous êtes enfant" )
    else:
        print("Vous êtes mineur")


     # afficher la taille
    if not taille == 0:
        print("Votre taille est " + str(taille) + " m" )


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input( nom_personne + " quel age avez vous ? ")
        try:
            age_int = int(age_str)
        except:
            print("Désolé il y'a une erreur!")
    return age_int

#####Variable Globale
# age = 0
#
# def demander_age():
#     global age
#     while age == 0:
#         age_str = input("Quel age avez vous ? ")
#         try:
#             age = int(age_str)
#         except:
#             print("Désolé il y'a une erreur!")

#######################################################
def demander_nom():

    nom_bis = ""

    while nom_bis == "" :
        nom_bis = input ("Quel est votre nom?")
    return nom_bis


#demander nom
nom1 = demander_nom()
nom2 = demander_nom()

# # demander age
age1 = demander_age(nom1)
age2 = demander_age(nom2)



#afficher resultats
afficher_informations_personne(nom1,age1)
afficher_informations_personne(nom2,age2)

# # boucle white : "tant que"...
# n = 0
# print(n)
# n = 12
# print(n)
# n = n + 1
# print(n)
#
# print("debut")
# while n < 10:
#     print("Valeur de n: " + str(n))
#     n = n + 1
#     print("fin")

# mdp = ""
# while not mdp == "Nadia":
#     mdp = input("Quel est le mdp ? ")
#
# print("Mdp oorrect vous avez accés à votre compte")

# boucle for
NB_PERSONNES = 1  #contante en majuscule

for i in range(0,NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom,age,1.75)