number = None
list_num = []

while True:
    try:
        num = input('Enter a number: ')
        if num == 'done' :
            break
            print(num)
        if number is None:
            num_new = int(num)
            list_num.append(num_new)
    except ValueError:
        print('Invalid input')

print('Maximum is', max(list_num))
print('Minimum is', min(list_num))
