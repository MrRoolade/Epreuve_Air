#~~> MrRøølåÐe <~~#
## Un seul à la fois
### un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents. 
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
if __name__ == "__main__":
    # Parsing
    user_value = sys.argv[1:]
    number_of_value = len(sys.argv)

    # Gestion des erreurs 
    def handle_error(): 
        try:
            if number_of_value <= 1 :
                raise ValueError
        except (ValueError, IndexError):
            quit_program()

    # Fonctions
    def delete_same_char(u_value): 
        new_string = ""
        if len(u_value) == 1:
            user_string = "".join(u_value)
        else:
            user_string = " ".join(u_value)
        length = len(user_string)
        for i in range(length):
            if user_string[i] != user_string[i-1]:
                new_string+= user_string[i]
        return new_string

    def quit_program():
        sys.exit("error")

    # Résolution
    handle_error()
    result= delete_same_char(user_value)

    # Affichage Résultat
    print(result)