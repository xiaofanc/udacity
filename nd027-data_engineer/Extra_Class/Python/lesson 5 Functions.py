lambda expression;
def double(x):
    return x**2
same:
double = lambda x: x**2
production = lambda x, y: x*y

Quiz: Lambda with Map
#map() is a higher-order built-in function that takes a function and iterable 
#as inputs, and returns an iterator that applies the function to each element 
#of the iterable. 
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
averages = list(map(lambda x: sum(x) / len(x), numbers))

print(averages)

Quiz: Lambda with Filter
#filter() is a higher-order built-in function that takes a function and iterable 
#as inputs and returns an iterator with the elements from the iterable for which 
#the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda x: len(x) < 10, cities))

print(short_cities)


Generator;
#https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def simple_generator_function():
   yield 1  #like return 
   yield 2
   yield 3

our_generator = simple_generator_function()
next(our_generator) # 1
next(our_generator) # 2
next(our_generator) # 3

