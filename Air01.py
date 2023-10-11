#~~> MrRøølåÐe <~~#
## Split en fonction
### un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.    
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

# Parsing
if __name__ == "__main__":
    user_value = sys.argv[1]
    separateur= sys.argv[-1]
    number_of_value = len(sys.argv)





    # Gestion des erreurs 
    def handle_error(): 
        try:
            if number_of_value <= 1 :
                raise ValueError
            if not is_string_in_string(user_value, separateur) :
                raise ValueError
        except (ValueError, IndexError):
            quit_program()

    # Fonctions
    def is_string_in_string(first_value, second_value):
        for i in range(len(first_value) - len(second_value) +1):
                if second_value == first_value[i: i +len(second_value)]:
                    return True
        return False

    def split_function(u_value,sep):
        word =''
        new_array = []
        length = len(sep)   
        for i in range(len(u_value)):
                if sep == u_value[i: i+length] :
                    new_array.append(word)
                    word = ''
                    i += length
                    index_fin_sep=i
                else:
                    word += u_value[i]
        new_array.append(u_value[index_fin_sep:])
        return new_array

    def quit_program():
        sys.exit("error_air301")

    # Résolution
    handle_error()
    result= split_function(user_value, separateur)

    # Affichage Résultat
    for string in result:
        print(string)