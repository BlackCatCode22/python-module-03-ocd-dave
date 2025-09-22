#####################################################################
#   * work_ex_05_02 *                                               #
#   Write a program which repeatedly reads integers until the user  #
#   enters “done”. Once “done” is entered, print out the min, and   #
#   of the integers. If the user enters anything other the an       #
#   integer, detect their mistake using try and except and print    #
#   and error message and skip to the next integers.                #
#####################################################################

tot = 0
num = 0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    tot += fval
    num += 1

if num > 0:
    print('Total: ', tot)
    print('Count: ', num)
    print('Average: ', tot/num)
else:
    print('No integers were entered. No total, count, or average to display!')

########################
# Enter a number: 7    #
# Enter a number: 2    #
# Enter a number: bob  #
# Invalid input        #
# Enter a number: 10   #
# Enter a number: 4    #
# Enter a number: done #
# Total:  23.0         #
# Count:  4            #
# Average:  5.75       #
########################
