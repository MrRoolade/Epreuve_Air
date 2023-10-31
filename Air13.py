#~~> MrRøølåÐe <~~#
## Le meta exo
### Programme qui vérifie si les exercices de votre épreuve de l’air sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là).
#### Créez au moins un test pour chaque exercice.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys ,os.path
import unittest
import importlib.util   

# Parsing
module_name = "Air"
module_number = 0
number_of_success = 0
module_number_format = "{:02d}".format(module_number)
module_name_complete = module_name + str(module_number_format)

while module_number !=13 :
    i=1
    class TestScript(unittest.TestCase):
        script_path = module_name_complete+".py"

        def test_script_present(self):
            # Vérifiez si le module est importable
            i = 1
            self.assertIsNotNone(importlib.util.find_spec(module_name_complete))
            print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')

        def test_script_runs(self):
            try:
                i = 2
                __import__(module_name_complete)
                result = module_name_complete.split_function('Bonjour les gars', " ")
                self.assertEqual(result, ['Bonjour', 'les', 'gars'])
                print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')
                i = 3
                result = module_name_complete.split_function('Bonjour les gars', "les")
                self.assertEqual(result, ['Bonjour', 'les', 'gars'])
                print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')
            except Exception as e:
                self.fail(f"Le script '{self.script_path}' a rencontré une erreur lors de l'exécution : {e}")
    module_number+=1

    
if __name__ == "__main__":
    unittest.main()
   
        # imported_module = __import__(module_name_complete)
        # print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')
        # number_of_success+=1
        # if module_name_complete("Bonjour les gars") == ["Bonjour","les", "gars"] :
        #     i=2
        #     print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m') 
        # else:
        #     i=2
        #     print(f'{module_name_complete} ({i}/3) \033[31mFAILURE\033[0m')
       
       
    # except (ModuleNotFoundError, ValueError):
    #         print("\033[31merrorAir13\033[0m")

 # separator=[' ', '\t', '\n']
        # value ="Bonjour les gars"
        # if Air00.split_function(value,separator) == ["Bonjour", "les", "gars"]:
        #     print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')
        #     number_of_sucess+=1
        # else :
        #     print(f'{module_name_complete} ({i}/3) \033[31mFAILURE\033[0m')
        #    
        
# Gestion des erreurs 
# def handle_error(): 
#     if len(sys.argv) < 2 or not os.path.exists(user_value):
#         quit_program()

# Fonctions
# def read_file(u_value): 
#     with open(u_value, "r") as f:
#         text = f.read()
#         f.close
#     return text

# def quit_program():
#     sys.exit("error")   

# Résolution
# handle_error()

# Affichage Résultat
