#~~> MrRøølåÐe <~~#
## Concat
### un programme transforme un tableau de chaînes de caractères en une seule chaîne de caractères.
# Espacés d’un séparateur donné en dernier argument au programme.   
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
if __name__ == "__main__":
    user_value = sys.argv[1:-1]
    number_of_value = len(sys.argv)
    separator = sys.argv[-1]

    # Gestion des erreurs 
    def handle_error(): 
        try:
            if number_of_value <= 3 :
                raise ValueError
        except (ValueError, IndexError):
            quit_program()

    # Fonctions
    def concatenation_function(u_value,sep):
        new_string =''
        for i in range(len(u_value)):
                if i != len(u_value)-1:
                    new_string += u_value[i] + sep
                else:
                    new_string += u_value[i]
        return new_string

    def quit_program():
        sys.exit("error")

    # Résolution
    handle_error()
    result= concatenation_function(user_value, separator)

    # Affichage Résultat
    print(result)