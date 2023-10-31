import os
import importlib
import unittest
import sys

# sys.stderr = open(os.devnull, 'w')

# class CustomTestResult(unittest.TextTestResult):
#     def addSuccess(self, test):
#         pass
#     def addFailure(self, test, err):
#         pass   
#     def addError(self, test, err):
#         pass

def is_module_importable(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

def main():
    # exercises = ['Air00','Air01','Air02','Air03','Air04','Air05','Air06']
    exercises = ['Air02']
    
    for exercise in exercises:
        if is_module_importable(exercise):
            print(f'{exercise} 0/3 \033[32mSUCCESS\033[0m')
            test_module = importlib.import_module(exercise)
            suite = unittest.TestLoader().loadTestsFromModule(test_module)
            runner = unittest.TextTestRunner(verbosity=2)#resultclass=CustomTestResult
            runner.run(suite)
        else:
            print(f'{exercise} 0/3 \033[31mFAILURE\033[0m')

if __name__ == "__main__":
    main()

# sys.stderr = sys.__stderr__ # if you still need the stderr stream