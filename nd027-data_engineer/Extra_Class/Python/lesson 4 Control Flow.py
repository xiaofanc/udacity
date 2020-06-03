names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)
#['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']

for name in names: # have to use range in order to replace the item
    name = name.lower().replace(" ", "_")

print(names)
#['Joey Tribbiani', 'Monica Geller', 'Chandler Bing', 'Phoebe Buffay']

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
#['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']


break/continue;
#break terminates a for-loop or while-loop;
#continue is to skip one iteration in for-loop or while-loop;

example 31;
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for prime in check_prime:
    for i in range(2, prime):
        if prime % i == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(prime, i, prime))
            break
    if i == prime - 1:
        print("{} IS a prime number".format(prime))      


zip;
zip returns an iterator that combines multiple iterables into one sequence of tuples. 
list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

for combinations in zip(letters, nums):
    print(combinations[0], combinations[1])

unzip;
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

example:
Quiz: Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
points = ["{}: {}, {}, {}".format(l,x,y,z) \
for l, x, y, z in zip(labels, x_coord, y_coord, z_coord)]
print(points)
for point in points:
    print(point)

points = list(zip(labels, x_coord, y_coord, z_coord))
print(points)
for point in points:
    print(point)

for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
for point in points:
    print(point)

Quiz: Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose) #((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))


enumerate;
enumerate is a built in function that returns an iterator of tuples containing 
indices and values of a list.

items = ["banana", "apple", "orange"]
for i, item in zip(range(len(items), items)):
    print(i, item)
=
for i, item in enumerate(items):
    print(i, item)

Quiz: Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, char in enumerate(cast):
    cast[i] = char + " " + str(heights[i])

print(cast)


list comprehension:
#You create a list comprehension with brackets [], including an expression to 
#evaluate for each element in an iterable. 
squares = [x**2 for x in range(9) if x % 2 == 0]
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

Quiz: Extract First Names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those 
# scored at scored at least 65.
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [key for key, value in scores.items() if value >= 65]
print(passed)







