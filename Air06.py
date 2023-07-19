#~~> MrRøølåÐe <~~#
## Contrôle de pass sanitaire
### un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_value = sys.argv[1:-1]
number_of_value = len(sys.argv)
condition_string = sys.argv[-1]

# Gestion des erreurs 
def handle_error(): 
    try:
        if number_of_value <= 1 :
            raise ValueError
    except (ValueError, IndexError):
        quit_program()

# Fonctions
def delete_if_condition(u_value, u_operator):
    for i in range(len(u_value)):
        u_value[i] = int(u_value[i]) + int(u_operator)
    return u_value


def quit_program():
    sys.exit("error")

# Résolution
handle_error()
result= delete_if_condition(user_value, condition_string)

# Affichage Résultat
print(result)