#~~> MrRøølåÐe <~~#
## Concat
### un programme transforme un tableau de chaînes de caractères en une seule chaîne de caractères.
# Espacés d’un séparateur donné en dernier argument au programme.   
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
import unittest
exercise = "Air02"

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

if __name__ == "__main__":
    # Parsing
    user_value = sys.argv[1:-1]
    number_of_value = len(sys.argv)
    separateur = sys.argv[-1]
    # Résolution
    handle_error()
    result= concatenation_function(user_value, separateur)

    # Affichage Résultat
    print(result)
    
class MonModuleDeTest(unittest.TestCase):

    def run_test(self, input_string, separateur, expected_result, test_number):
        result = concatenation_function(input_string, separateur)
        try :
            self.assertEqual(result,expected_result)
            print(f'{exercise} {test_number}/3 \033[32mSUCCESS\033[0m')
        except AssertionError:
            print(f'{exercise} {test_number}/3 \033[31mFAILURE\033[0m')
            print(result,expected_result)

    def test1_concat_with_spaces(self):
        self.run_test(["je","teste"]," ","je teste", 1)

    def test2_concat_with_coma(self):
        self.run_test(["Suivre la fumée" , "des fraises"], ",", 'Suivre la fumée,des fraises', 2)

    def test3_split_empty_strings(self):
        self.run_test("123","","error", 3)