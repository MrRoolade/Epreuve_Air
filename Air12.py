#~~> MrRøølåÐe <~~#
## Le roi des tris
### Programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_array = sys.argv[1:]

# Gestion des erreurs 
def handle_error(): 
    if len(sys.argv) < 2 :
        quit_program("error")
    try:        
        user_array_int = [int(value) for value in user_array]
    except (ValueError, IndexError):
        quit_program("error")

# Fonctions
def quick_sort_array(array):
    if len(array)<= 1:
        return array
    pivot = int(array[len(array)//2])
    array_low=[x for x in array if int(x)< pivot]
    array_high=[x for x in array if int(x) > pivot]
    middle=[x for x in array if int(x) == pivot]
    return quick_sort_array(array_low) + middle + quick_sort_array(array_high)
    
def quit_program(message):
    sys.exit(message)   

# Résolution
handle_error()
result = quick_sort_array(user_array)

# Affichage Résultat
for i in result:
    print(i, end=" ")