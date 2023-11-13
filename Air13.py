#~~> MrRøølåÐe <~~#
""" Le meta exo
 Programme qui vérifie si les exercices de votre épreuve de l'air sont présents dans le répertoire et qu'ils fonctionnent (sauf celui là).
 Créez au moins un test pour chaque exercice.
 Afficher error et quitter le programme en cas de problèmes d'arguments"""

import subprocess

def generate_exercise_names(module_name, num_exercises):
    return [f"{module_name}{num:02d}.py" for num in range(0,num_exercises)]

def execute_test(arg):
    process = subprocess.Popen(arg, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output, error

def compare_result(output, expected):
    if isinstance(expected, str):
        # Si la valeur attendue est une chaîne, compare sans tenir compte des espaces et des retours à la ligne
        return output.strip() == expected.strip()
    elif isinstance(expected, list):
        # Si la valeur attendue est une liste, compare les éléments après avoir joint avec des retours à la ligne
        return output.strip() == "\n".join(expected)
     
def display_result(result: bool):
    if result: 
        print(f'\033[32mSUCCESS\033[0m')
    else:
        print(f'\033[31mFAILURE\033[0m')

def run_tests():
    module_name = "Air"
    exercises = generate_exercise_names(module_name, 13)
    success_count = {}  
    exercise_count = {} 

    input_exo = {
        "00": (["Bonjour les gars"]),
        "00_1": (["Bonjour les filles"]),
        "01": (["Bonjour les gars", "les"]),
        "01_1": (["Bonjour les filles", "les"]),
        "02": (["je","teste", "des", "trucs", "/"]),
        "02_1": (["je","suis", "chaud", "zzzzz!"]),
        "03": (["1", "2", "3", "4", "5", "4", "3", "2", "1"]),
        "03_1": (["monsieur", "fifou", "fifou", "michel", "michel"]),
        "04": (["Hello milady,   bien ou quoi !!"]),
        "04_1": (["Sallut, biieen !!"]),
        "05": (["1", "2", "3", "4", "5", "+2"]),
        "05_1": (["3", "4", "5", "-2"]),
        "06": (["Michel", "Albert", "Thérèse", "Benoit", "t"]),
        "07": (["10", "20", "30", "40", "50", "33"]),
        "08": (["10", "20", "30", "fusion", "15", "25", "35"]),
        "09": (["Michel", "Albert", "Benoît", "Bernadette"]),
        "10": (["a.txt"]),
        "11": (["O", "5"]),
        "11_1": (["Y", "4"]),
        "12": (["6", "5", "4", "3", "2", "1"]),
        "12_1": (["15", "8", "74", "23", "42", "11"]),
    }

    output_exo = {
        "00": (["Bonjour", "les", "gars"]),
        "00_1": (["Bonjour", "les", "filles"]),
        "01": (["Bonjour ", " gars"]),
        "01_1": (["Bonjour ", " fil"]),
        "02": ("je/teste/des/trucs"),
        "02_1": ("jezzzzz!suiszzzzz!chaud"),
        "03": ("5"),
        "03_1": ("monsieur"),
        "04": ("Helo milady, bien ou quoi !"),
        "04_1": ("Salut, bien !"),
        "05": ("3 4 5 6 7"),
        "05_1": ("1 2 3"),
        "06": ("Michel"),
        "07": ("10 20 30 33 40 50"),
        "08": ("10 15 20 25 30 35"),
        "09": ("Albert Benoît Bernadette Michel"),
        "10": ("Je danse le mia"),
        "11": ("    O\n   OOO\n  OOOOO\n OOOOOOO\nOOOOOOOOO"),
        "11_1": ("   Y\n  YYY\n YYYYY\nYYYYYYY"),
        "12": ("1 2 3 4 5 6"),
        "12_1": ("8 11 15 23 42 74"),
    }

    #compte le nombre de test par exercice
    for num in output_exo.keys():
        num = num[:2]
        if num in exercise_count:
            exercise_count[num] += 1
        else:
            exercise_count[num] = 1
           
    for exercise in exercises:
        test_number = 1
        for test_key, arg1 in input_exo.items():
            if exercise[-5:-3].endswith(test_key[:2]):
                print(f"Air{exercise[-5:-3]} {test_number:02d}/{exercise_count[exercise[-5:-3]]:02d} ",end=" ")
                arg1 = input_exo.get(test_key,str)
                expected_result = output_exo.get(test_key, [str])
                arguments = ['python3', exercise, *arg1]
                actual_output, error = execute_test(arguments)
                result = compare_result(actual_output, expected_result )
                display_result(result)
                success_count[test_key] = result
                test_number += 1
    print(f'Total success: {sum(success_count.values())}/{len(input_exo)}')

if __name__ == "__main__":
    run_tests()