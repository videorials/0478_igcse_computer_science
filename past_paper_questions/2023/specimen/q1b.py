import helper as helper

# >> ------------------------------------ << import and return all data from file to array >>
Names = helper.load_qty_to_array("names.txt", 50)
# Names = helper.load_to_array("names.txt")

'''
# >> -------------------- << question >>
Using a single loop, write an algorithm in pseudocode to
output 50 names that have been stored in the array, Name[]

# >> -------------------- << pseudocode >>
FOR Index ← 1 TO LENGTH(Names)
    OUTPUT Names[Index]
NEXT Index

Count ← 0
WHILE Count < LENGTH(Names) DO
    OUTPUT Names[Count]
    Count ← Count + 1
ENDWHILE

Count = 0
REPEAT
    OUTPUT Names[Count]
    Count ← Count + 1
UNTIL Count > LENGTH(Names)
'''

# >> -------------------- << code >>
for Index in range(0,len(Names)):
    print(Names[Index])

Count = 0
while Count < len(Names):
    print(Names[Count])
    Count = Count + 1

Count = 0
while True:
    print(Names[Count])
    Count = Count + 1
    if Count >= len(Names):
        break