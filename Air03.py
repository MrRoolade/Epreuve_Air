#~~> MrRøølåÐe <~~#
## Chercher l’intrus
### un programme qui retourne la valeur d’une liste qui n’a pas de paire. 
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)

# Gestion des erreurs 
def handle_error(): 
    try:
        if number_of_value <= 2 :
            raise ValueError
    except (ValueError, IndexError):
        quit_program()

# Fonctions
def no_pair_function(u_value):
    solo = []
    for value in u_value:
        count = u_value.count(value)
        if count % 2 != 0:
            solo.append(value)
    if solo == []:
        solo.append("pas d'intrus")
    return " ".join(solo)

def quit_program():
    sys.exit("error")

# Résolution
handle_error()
result= no_pair_function(user_value)

# Affichage Résultat
print(result)