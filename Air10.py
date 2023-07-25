#~~> MrRøølåÐe <~~#
## Afficher le contenu
### un programme qui affiche le contenu d’un fichier donné en argument.
#### Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.

import sys ,os.path

# Parsing
user_value = "".join(sys.argv[1:])

# Gestion des erreurs 
def handle_error(): 
    if len(sys.argv) < 2 :
        quit_program()

# Fonctions
def read_file(u_value): 
    with open(u_value, "r", encoding ="cp1252") as f:
        text = f.read()
        f.close
    return text

def quit_program():
    sys.exit("error")   

# Résolution
handle_error()
result= read_file(user_value)

# Affichage Résultat
print(result)