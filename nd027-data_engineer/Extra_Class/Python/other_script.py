print(2+3)

num = 3*4

def mean(s):
    return sum(s) / len(s)

def add_five(num_list):
    return [n + 5 for n in num_list]

"""
# run only when the main program being executed is this other_script.py
# avoid running executable statements in a script when it's imported as a module in another script

if __name__ == '__main__': 
    print("test mean functions: ")   
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean) 

same:
but main() function can be called in another script if other_script is imported
"""
def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()