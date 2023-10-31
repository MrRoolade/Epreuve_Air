#~~> MrRøølåÐe <~~#
## Split
### un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
import unittest
exercise = "Air00"
string_separateur=[' ', '\t', '\n']
    
# Gestion des erreurs 
def handle_error(argument):
    if len(argument) != 1 :
        quit_program()

# Fonctions
def split_function(user_value, string_separateur=[' ', '\t', '\n']):
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
if __name__ == '__main__':
    user_value = sys.argv[1:]
    number_of_value = len(sys.argv)
    string_separateur=[' ', '\t', '\n']
    
    # Résolution
    handle_error(user_value)
    result= split_function(user_value , string_separateur)

    # Résultat
    for string in result:
        print(string)

#module de test
class MonModuleDeTest(unittest.TestCase):

    def run_test(self, input_string, expected_result, test_number):
        result = split_function(input_string)
        try :
            self.assertEqual(result,expected_result)
            print(f'{exercise} {test_number}/3 \033[32mSUCCESS\033[0m')
        except AssertionError:
            print(f'{exercise} {test_number}/3 \033[31mFAILURE\033[0m')

    def test1_split_with_spaces(self):
        self.run_test("Bonjour les gars",['Bonjour', 'les', 'gars'], 1)

    def test2_split_with_tabs(self):
        self.run_test("Bonjour\tles\tgars",['Bonjour', 'les', 'gars'], 2)

    def test3_split_empty_strings(self):
        self.run_test("",[], 3)