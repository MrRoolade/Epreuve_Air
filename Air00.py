#~~> MrRøølåÐe <~~#
## Split
### un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def split_function(user_value, string_separateur):
    word =''
    new_array = []
    user_value = "".join(user_value)
    for i in range(len(user_value)):
        if user_value[i] in string_separateur :
            if word!='':
                new_array.append(word)
                word =''
        else:
            word += user_value[i]
    if word!='':
        new_array.append(word)
    return new_array

def quit_program():
    sys.exit("error")

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)
string_separateur=[' ', '\t', '\n']
  
# Gestion des erreurs 
try:
   if number_of_value <= 1 :
        raise ValueError
except (ValueError, IndexError):
        quit_program()

# Résolution
result= split_function(user_value , string_separateur)

# Résultat
for word in result:
    print(word)