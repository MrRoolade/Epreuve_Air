#~~> MrRøølåÐe <~~#
## Afficher une pyramide
### Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys ,os.path

# Parsing
user_value = sys.argv[1:]
pattern = user_value[0]
number_floor = user_value[1]

# Gestion des erreurs 
def handle_error(): 
    try:
        if len(sys.argv) != 3 or not user_value[1].isdigit():
            quit_program()
    except (ValueError, IndexError):
        quit_program()

# Fonctions
def make_pyramide(motif, number): 
    number=int(number)
    for i in range(1,number+1):
        space = (number-i)*" "
        block = (2*i-1)*motif
        pyramid=(space+block)
        print(pyramid)

def quit_program():
    sys.exit("error")   

# Résolution
handle_error()


# Affichage Résultat
make_pyramide(pattern , number_floor)