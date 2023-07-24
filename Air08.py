#~~> MrRøølåÐe <~~#
## Mélanger deux tableaux triés
### un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.
#### Le dernier argument est l’élément à ajouter.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_value = sys.argv[1:]

# Gestion des erreurs 
def handle_error(): 
    if len(sys.argv) <= 2 or user_value.count("fusion")!=1:
        quit_program()

    origin_array = [value for value in user_value if value!= "fusion"]
    for value in origin_array:
        if not value.isdigit():
            quit_program()

# Fonctions
def mix_array_sorted(f_array, s_array):
    new_array = []
    i, j = 0,0  
    while i != len(f_array) and j != len(s_array):
        if f_array[i] < s_array[j]:
            new_array.append(f_array[i])
            i+=1
        else:
            new_array.append(s_array[j])
            j+=1
    while i != len(f_array) :
        new_array.append(f_array[i])
        i+=1
    while j != len(s_array) :
        new_array.append(s_array[j])
        j+=1
    return new_array

# def easy_mix_array_sorted(f_array, s_array):
#     return sorted(f_array + s_array)

def quit_program():
    sys.exit("error")

# Résolution
handle_error()
pos_fusion = user_value.index("fusion")
first_array = [int(user_value[i]) for i in range(0,pos_fusion) ] 
second_array = [int(user_value[i]) for i in range(pos_fusion+1,len(user_value))]
result= mix_array_sorted(first_array, second_array)

# Affichage Résultat
print(result)