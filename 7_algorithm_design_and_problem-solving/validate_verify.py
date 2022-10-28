# https://www.computerscience.gcse.guru/theory/validation
# >> -------------------- << range check >>
def in_range(target, lower, upper):
    if target >= lower and target <= upper:
        return True
    else:
        return False


# >> -------------------- << length check >>
def valid_password_length(password, set_length):
    if len(password) < set_length:
        return False
    else:
        return True


# >> -------------------- << type check >>
def is_integer(number):
    if isinstance(number, int):
        return True
    else:
        return False


# >> -------------------- << presence check >>
def empty_password(password):
    if password == '':
        return True
    else:
        return False


# >> -------------------- << format check >>
def valid_date_formatted(date_string):

    if len(date_string) == 10:
        if date_string[2] == '/' and date_string[5] == '/':
            return True
        else:
            return False


# >> -------------------- << check digit >>
def valid_ean(barcode):
    total = 0
    for index in range(0, len(barcode) -1):
        integer = int(barcode[index])
        if index % 2 == 0:
            # The 1st, 3rd, 5th, and 7th digits are multiplied by three, and added to the total.
            total = total + (3 * integer)
        else:
            # The remaining numbers are added to the total.
            total = total + integer
    # The total is divided by ten.
    # The check digit is determined by subtracting the remainder from ten.
    check_digit = 10 - (total % 10)

    if barcode[-1] == str(check_digit):
        return True
    else:
        return False
# check_digit = '2'
# ean_barcode = '2142345' + check_digit
# print(valid_ean(ean_barcode))


# >> -------------------- << visual check >>
def get_username():
    verified = False
    username = input("Enter username: ")
    while not verified:
        print("You entered the username: ", username )
        verify = input("Is this correct (Y/N): ").upper()
        if verify == 'Y':
            verified = True
        else:
            username = input("Please re-enter username: ")
    return username
# print(get_username())


# >> -------------------- << double entry >>
def get_password():
    verified = False
    password_one = input("Enter password: ")
    password_two = input("Verify password: ")

    while not verified:
        if password_one == password_two:
            verified = True
        else:
            password_one = input("Re-enter password: ")
            password_two = input("Verify password: ")

    return password_one
# print(get_password())