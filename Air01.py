#~~> MrRøølåÐe <~~#
## Split en fonction
### un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.    
##### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys
import unittest

# Variable du module 
exercise="Air01"

# Parsing 1/2
number_of_value = len(sys.argv)

# Gestion des erreurs 
def handle_error(): 
    try:
        separateur= sys.argv[-1]
        user_value = sys.argv[1]
        if number_of_value != 3 or not is_string_in_string(user_value, separateur) :
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
    temp =''
    i=0
    new_array = []
    length = len(sep)   
    while i < (len(u_value)):
        if u_value[i: i+length] == sep :
            new_array.append(temp)
            temp = ''
            i += length
        else:
            temp += u_value[i]
            i+=1
    if temp !="":
         new_array.append(temp)
    return new_array

def quit_program():
    sys.exit("error")

if __name__ == "__main__":
    #Parsing 2/2
    separateur= sys.argv[-1]
    user_value = sys.argv[1]

     # Résolution
    handle_error()
    result= split_function(user_value, separateur)

    # Affichage Résultat
    for string in result:
        print(string)

class MonModuleDeTest(unittest.TestCase):

    def run_test(self, input_string,separateur, expected_result, test_number):
        result = split_function(input_string,separateur)
        try :
            self.assertEqual(result,expected_result)
            print(f'{exercise} {test_number}/3 \033[32mSUCCESS\033[0m')
        except AssertionError:
            print(f'{exercise} {test_number}/3 \033[31mFAILURE\033[0m')

    def test1_split_with_spaces(self):
        self.run_test("Bonjour les gars", "les",['Bonjour ', ' gars'], 1)

    def test2_split_with_tabs(self):
        self.run_test("Suivre la fumée des fraises des jalous","des", ['Suivre la fumée ',' fraises ',' jalous'], 2)

    def test3_split_empty_strings(self):
        self.run_test("","",[], 3)