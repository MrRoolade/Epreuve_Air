#~~> MrRøølåÐe <~~#
## Le roi des tris
### Programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
user_array = sys.argv[1:]
arr = []

# Gestion des erreurs 
def handle_error(): 
    try:
        if len(sys.argv) < 2 :
            quit_program("error")
    except (ValueError, IndexError):
        quit_program("error")

# Fonctions
def quick_sort_array(arr):
    if len(arr)<= 1:
        return arr
    pivot = arr[int(len(arr)/2)]
    arr_low=[x for x in arr if x < pivot]
    arr_high=[x for x in arr if x > pivot]
    middle=[x for x in arr if x == pivot]
    return quick_sort_array(arr_low) + middle + quick_sort_array(arr_high)

    
def quit_program(message):
    sys.exit(message)   

# Résolution
handle_error()

# Affichage Résultat
print(quick_sort_array(user_array))