#~~> MrRøølåÐe <~~#
## Insertion dans un tableau trié
### un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant.
#### Le dernier argument est l’élément à ajouter.
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

if __name__ == "__main__":
    # Parsing
    user_value = sys.argv[1:-1]
    number_of_value = len(sys.argv)
    insert_value = sys.argv[-1]

    # Gestion des erreurs 
    def handle_error(): 
        try:
            if number_of_value <= 2 :
                raise ValueError
            for value in user_value:
                if not value.isdigit()or not insert_value.isdigit():
                    raise ValueError
        except (ValueError, IndexError):
            quit_program()

    # Fonctions
    def insert_value_sorted(u_value, insert):
        new_array = []
        for i in range(0,len(u_value)+1):
            if u_value[i] < insert :
                new_array.append(u_value[i])
            else:
                new_array.append(insert)
                new_array.extend(u_value[i:len(u_value)])
                break
        return new_array

    def quit_program():
        sys.exit("error")

    # Résolution
    handle_error()
    result= insert_value_sorted(user_value, insert_value)

    # Affichage Résultat
    print(" ".join(result))