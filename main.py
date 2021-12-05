nom = input("Quel est ton nom ? ")

age = 0
while age == 0:
    age_str = input("Quel age avez vous ? ")
    try:
        age = int(age_str)
    except:
        print("Désolé il y'a une erreur!")

# print("fin")
print("Vous vous apeller " + nom + " et vous avez " + str(age) + " ans.")
print("L'année prochaine " + nom + " vous allez avoir " + str(age + 1) + "ans.")


# # boucle white : "tant que"...
n = 0
print(n)
n = 12
print(n)
n = n + 1
print(n)

print("debut")
while n < 10:
    print("Valeur de n: " + str(n))
    n = n + 1
    print("fin")

# mdp = ""
# while not mdp == "Nadia":
#     mdp = input("Quel est le mdp ? ")
#
# print("Mdp oorrect vous avez accés à votre compte")