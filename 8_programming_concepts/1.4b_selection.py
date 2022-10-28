# >> selection
'''
>> including: WHILE, IF, CASE
'''
# >> ----------------------------- << example code >>
# input integer...output colour
col_code = 0
while col_code < 1 or col_code > 3:
    col_code = int(input('Enter colour code (1, 2, 3): '))

if col_code == 1:
    print('IF | Red')
elif col_code == 2:
    print('IF | Amber')
elif col_code == 3:
    print('IF | Green')
elif col_code == 9:
    print('IF | Admin')
else:
    print('IF | Enter a valid number dummy!')

match col_code:
    case 1: print('CASE | Red')
    case 2: print('CASE | Amber')
    case 3: print('CASE | Green')
    case 9: print('CASE | Admin...')
    case _: print('CASE | Enter a valid number dummy!')