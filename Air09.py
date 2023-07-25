#~~> MrRøølåÐe <~~#
##Rotation vers la gauche
### un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_value = sys.argv[1:]

# Gestion des erreurs 
def handle_error(): 
    if len(sys.argv) <= 2 :
        quit_program()

# Fonctions
def rotate_to_the_left(u_value):
    new_array=[]
    for i in range(1,len(u_value)):
        if u_value[i]!=0 :
            new_array.append(u_value[i])
    new_array.append(u_value[0])
    
    return new_array

def quit_program():
    sys.exit("error")

# Résolution
handle_error()
result= rotate_to_the_left(user_value)

# Affichage Résultat
print(", ".join(result))