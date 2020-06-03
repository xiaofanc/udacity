#The input function takes in whatever the user types and stores it as a string.
name = input('Enter a name: ')
print('Hello ', name.title())

number = int(input('Enter a number: '))
number += 10
print(number)

#interpret user input as a Python expression using the built-in function eval
result = eval(input("Enter an expression: "))
print(result)

names = input("Enter names separated by commas: ").title().split(",")# get and process input for a list of names
assignments =  input("Enter assignment counts separated by commas: ").split(",")# get and process input for a list of the number of assignments
grades =  input("Enter grades separated by commas: ").split(",")# get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for s, a, g in zip(names, assignments, grades):
    print(message.format(s, a, g, int(g)+int(a)*2))

