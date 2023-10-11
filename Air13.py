#~~> MrRøølåÐe <~~#
## Le meta exo
### Programme qui vérifie si les exercices de votre épreuve de l’air sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là).
#### Créez au moins un test pour chaque exercice.
#### Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys ,os.path

# Parsing
module_number = 00
module_name = "Air"
number_of_success = 0
i=1

while module_number !=13 :
    module_number_format = "{:02d}".format(module_number)
    module_name_complete = module_name + str(module_number_format)
    try :
        imported_module = __import__(module_name_complete)
        print(f'{module_name_complete} ({i}/3) \033[32mSUCCESS\033[0m')
        number_of_success+=1
        module_number+=1
       
    except (ModuleNotFoundError, ValueError):
            print("\033[31merrorAir13\033[0m")

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
