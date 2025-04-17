# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from modulefinder import Module
from utilitiesPackage.utilities import *

if __name__ == "__main__":
    print("Starting...")
    from groupPackage.test import *
    module_names, modules = run_modules_in_package("groupPackage")

    #print("Modules that were loaded:")
    #for module in modules:
    #    print(module)

    expected_function = "get_favorite_food"   # No parens should be used here
    favorite_foods = dict()
    success_count = 0
    failure_count = 0
    for module in modules:
        #print(module)
        attributes = sorted(dir(module))
        module_name = module.__str__().split("\\\\")[-1][:-2]
        #if attributes:
        #    for attribute in attributes:
        #        print(attribute)
        try:
            function = getattr(module, expected_function)
            if callable(function):
                print("Executing", expected_function + "()", "in", module.__str__().split("\\\\")[-1][:-2])
                try:
                    favorite_food = getattr(module, expected_function)()
                    favorite_foods[module_name] = favorite_food
                    success_count = success_count + 1
                    #print("  favorite food is", favorite_food)
                except Exception as e:
                    print(e)
                    failure_count = failure_count + 1
        except Exception as e:
            print(e)
            failure_count = failure_count + 1
    print("Success count: ", success_count, "Failure count:", failure_count)
    print("Favorite Foods:")
    print(favorite_foods)