while Ture:
    try:
        num = int(input('Enter a number: '))
        break
    except:  # when any kind of exceptions occur
        print('That\'s not a valid number!')
    print('\nAttempted Input\n') # will not print if number is true since break

while Ture:
    try:
        num = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n') # will always print regardless of break

while Ture:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:   # only handle the ValueError exception
    # except (ValueError, KeyboardInterrupt)
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n') # will always print regardless of break

while Ture:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:   # only handle the ValueError exception
        print('That\'s not a valid number!')
    except KeyboardInterrupt:  # handle keyboardinterrupt exception
        print('\nNo input taken')
        break
    finally:
        print('\nAttempted Input\n') # will always print regardless of break

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
   
# addtional info from pythonds
if anumber < 0:
   raise RuntimeError("You can't use a negative number")
else:
   print(math.sqrt(anumber))



def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except:
        print("People number is not valid")

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")



    