#~~> MrRøølåÐe <~~#
## Chercher l’intrus
### un programme qui retourne la valeur d’une liste qui n’a pas de paire. 
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
import unittest
exercise = "Air03"

# Parsing
user_value = sys.argv[1:]
number_of_value = len(sys.argv)

# Gestion des erreurs 
def handle_error(): 
    try:
        if number_of_value <= 2 :
            raise ValueError
    except (ValueError, IndexError):
        quit_program()

# Fonctions
def no_pair_function(u_value):
    solo = []
    for value in u_value:
        count = u_value.count(value)
        if count % 2 != 0:
            solo.append(value)
    if solo == []:
        solo.append("pas d'intrus")
    return " ".join(solo)

def quit_program():
    sys.exit("error")

def main():
    # Résolution
    handle_error()
    result= no_pair_function(user_value)

    # Affichage Résultat
    print(result)

if __name__ == "__main__":
    main()

class MonModuleDeTest(unittest.TestCase):

    def run_test(self, input_value, expected_result, test_number):
        result = no_pair_function(input_value)
        try :
            self.assertEqual(result,expected_result)
            print(f'{exercise} {test_number}/3 \033[32mSUCCESS\033[0m')
            print(result,expected_result)
        except AssertionError:
            print(f'{exercise} {test_number}/3 \033[31mFAILURE\033[0m')
            print(result,expected_result)

    def test1_no_pair_with_strings(self):
        self.run_test(["Bonjour","Bonjour", "Michou"],"Michou", 1)

    def test2_no_pair_with_number(self):
        self.run_test(["1","2","3","4","5","4","3","2","1"],"4", 2)