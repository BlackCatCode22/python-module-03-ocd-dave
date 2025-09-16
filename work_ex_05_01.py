num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval

# print('ALL DONE')
print(tot,num,tot/num)

#############################
#   Enter a number: 4       #
#   4.0                     #
#   Enter a number: 5       #
#   5.0                     #
#   Enter a number: 6       #
#   6.0                     #
#   Enter a number: qwerty  #
#   invalid input           #
#   Enter a number: qwerty  #
#   invalid input           #
#   Enter a number: qwerty  #
#   invalid input           #
#   Enter a number: done    #
#   15.0 3 5.0              #
#############################
