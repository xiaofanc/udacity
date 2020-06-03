# Write your code here
# HINT: create a dictionary from flowers.txt
flower_dict = {}
with open('flowers.txt') as f:
    for line in f:
        flower_dict[line.strip().split(':')[0]] = line.strip().split(':')[1]
#print(flower_dict)

# HINT: create a function to ask for user's first and last name
def input_name():
    x = input("Enter your First [space] Last name only: ")
    f_name = flower_dict[x.split()[0][0].capitalize()]
    if f_name:
        print("Unique flower name with the first letter: {}".format(f_name))
   
input_name()

# answer
# function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()

