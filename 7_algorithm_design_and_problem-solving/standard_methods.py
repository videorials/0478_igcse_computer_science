import sys # use to get largest integer
unsorted_integers = [1,9,4,7,5,6,3,8,2]

# >> -------------------- << linear search >>
target = 7
def linear_search(target, collection):
    for index in range(0, len(collection)):
        if target == collection[index]:
            return index
    return False


# >> -------------------- << bubble sort >>
def bubble_sort(collection):
    for n in range(0, len(collection)-1):
        for index in range(0, len(collection)-1):
            value_one = collection[index]
            value_two = collection[index + 1]
            if value_one > value_two:
                collection[index] = value_two
                collection[index + 1] = value_one
    return collection


# >> -------------------- << totaling >>
def total(collection):
    total = 0
    for index in range(0, len(collection)):
        total = total + collection[index]
    return total


# >> -------------------- << counting >>
def count_evens(collection):
    count = 0
    for index in range(0, len(collection)):
        if collection[index] % 2 == 0:
            count = count + 1
    return count


# >> -------------------- << maximum >>
def get_max_value(collection):
    max = 0
    for index in range(0, len(collection)):
        if collection[index] > max:
            max = collection[index]
    return max


# >> -------------------- << minimum >>
def get_min_value(collection):
    min = sys.maxsize
    for index in range(0, len(collection)):
        if collection[index] < min:
            min = collection[index]
    return min


# >> -------------------- << average >>
def get_average(collection):
    total = 0
    for index in range(0, len(collection)):
        total = total + collection[index]
    return total / len(collection)