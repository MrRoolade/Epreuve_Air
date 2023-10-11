#~~> MrRøølåÐe <~~#
## Sur chacun d’entre eux
### un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
if __name__ == "__main__":
    # Parsing
    user_value = sys.argv[1:-1]
    number_of_value = len(sys.argv)
    operator = sys.argv[-1]

    # Gestion des erreurs 
    def handle_error(): 
        try:
            int(sys.argv[-1])
            for i in range(number_of_value-2):
                if number_of_value <= 1 or not user_value[i].isdigit() :
                    raise ValueError
        except (ValueError, IndexError):
            quit_program()

    # Fonctions
    def add_or_substract(u_value, u_operator):
        for i in range(len(u_value)):
            u_value[i] = int(u_value[i]) + int(u_operator)
        return u_value


    def quit_program():
        sys.exit("error")

    # Résolution
    handle_error()
    result= add_or_substract(user_value, operator)

    # Affichage Résultat
    for nb in result:
        print(nb, end=" ")