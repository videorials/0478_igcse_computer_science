# >> iteration
'''
>> including: count-controlled loops, pre-condition loops, post-condition loops
>> !! exam board pseudocode only supports FOR looping <value> TO <value> !!
>> !! python does not support DO WHILE loops !!
'''
# >> ----------------------------- << example code >>
string = 'Andrew'
array = [2,6,3,9,6]

# for | items in collection
print("FOR | items in a collection")
for item in string:
  print(item)

# for | loop index from zero to...
print("FOR | index from zero to...")
for i in range(5):
  print(i, array[i])

# for | index starting from and to...
print("FOR | index starting from and to...")
for i in range(2,5):
  print(i, array[i])

# for | loop conting between range in positive and negative increments
print("FOR | index starting from and to, in crements of...")
for i in range(len(array)-1,-1,-1):
  print(i, array[i])

# while
print("WHILE loop")
iterate = len(array)-1
while iterate >= 0:
  print(iterate, array[iterate])
  iterate -= 1

# do while
secret_word = ''
counter = 0
while True:
  if secret_word == 'zen':
    print('Welcome')
    break
  elif counter == 5:
    print('You ran out of tries')
    break
  else:
    secret_word = input('What is the secret word? ')
    counter += 1