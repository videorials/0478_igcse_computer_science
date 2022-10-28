# >> 3 Understand and use input and output
'''
'''
# >> ----------------------------- << example code >>
users = ["bramwax","parhapx","andernx","bucklzx"]
while True:
    username = input("Enter your username: ")
    if username in users:
        print("Hello", username)
        break
    else:
        print("Username not recognised...")