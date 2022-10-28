import random

# >> ------------------------------------ << arrays >>
'''
DECLARE StudentNames : ARRAY[1:30] OF STRING
StudentNames ← "Ali"
StudentNames[n+1] ← StudentNames[n]

DECLARE NoughtsAndCrosses[1:3, 1:3] OF CHAR
NoughtsAndCrosses[2,3] ← 'X'
'''
StudentNames = []
for index in range(0,30):
    StudentNames.append(None)
StudentNames[0] = "Ali"
StudentNames[0+1] = StudentNames[0]
print(StudentNames)

NoughtsAndCrosses = []
for list in range(0,3):
    columns = []
    for column in range(0,3):
        columns.append(None)
    NoughtsAndCrosses.append(columns)
NoughtsAndCrosses[1][2] = 'X'
print(NoughtsAndCrosses)


# >> --------------------- << arithmetic operations >>
'''
Bits ← 2 ^ 5
AnswerOne ← DIV(10, 3) returns 3
AnswerTwo ← MOD(10, 3) returns 1
'''
Bits = 2 ** 5
AnswerOne = 10 // 3
AnswerTwo = 10 % 3
print(Bits, AnswerOne, AnswerTwo)


# >> -------------- << logical & boolean operations >>
'''
IF Answer < 0 OR Answer > 100 AND Answer != 50
    THEN
        Correct ← FALSE
    ELSE
        Correct ← TRUE
ENDIF
'''
def valid_integer(integer):
    if Answer >= 0 and Answer <= 100 and Answer != 50:
        return True
    else:
        return False
Answer = 50
print(valid_integer(Answer))

# >> ------------------------- << string operations >>
'''
LENGTH("Happy Days" will return 10)
LCASE('W') will return 'w'
UCASE("Happy") will return "HAPPY"
SUBSTRING("Happy Days", 1, 5) will return "Happy"
'''
print(len("Happy Days"))
print("W".lower())
print("Happy".upper())
print("Happy Days"[0:5])


# >> --------------------------- << library routnes >>
'''
Value ← ROUND (RANDOM() * 6, 0) // returns whole number between 0 and 6
'''
Value = round(random.random() * 6)
print(Value)

# >> --------------------- << selection | if...else >>
'''
IF ChallengerScore > ChampionScore
    THEN
        IF ChallengerScore > HighestScore
            THEN
                OUTPUT ChallengerName, " is champion and highest scorer"
            ELSE
                OUTPUT Player1Name, " is the new champion"
        ENDIF
    ELSE
        OUTPUT ChampionName, " is still the champion"
        IF ChampionScore > HighestScore
            THEN
                OUTPUT ChampionName, " is also the highest scorer"
        ENDIF
ENDIF
'''
ChallengerName = "Jane"
ChallengerScore = 66
ChampionName = "Justine"
ChampionScore = 76
Player1Name = "Janet"
HighestScore = 82

if ChallengerScore > ChampionScore:
    if ChallengerScore > HighestScore:
        print(ChallengerName, " is champion and highest scorer")
    else:
        print(Player1Name, " is the new champion")
else:
    print(ChampionName, " is still the champion")
    if ChampionScore > HighestScore:
        print(ChampionName, " is also the highest scorer")


# >> ----------------------------- << select | case >>
'''
INPUT Move
CASE OF Move
    'W' : Position ← Position - 10
    'E' : Position ← Position + 10
    'A' : Position ← Position - 1
    'D' : Position ← Position + 1
    OTHERWISE OUTPUT "Beep"
ENDCASE
'''
Move = input("Next move: ")
Position = 0
match Move:
    case 'W':
        Position = Position - 10
    case 'E':
        Position = Position - 10
    case 'A':
        Position = Position - 10
    case 'D':
        Position = Position - 10
    case   _:
        print("Beep")


# >> --------------------------- << iteration | for >>
'''
Total ← 0
FOR Row ← 1 TO MaxRow
    RowTotal ← 0
    FOR Column ← 1 TO 10
        RowTotal ← RowTotal + Amount[Row, Column]
    NEXT Column
    OUTPUT "Total for Row ", Row, " is ", RowTotal
    Total ← Total + RowTotal
NEXT Row
OUTPUT "The grand total is ", Total
'''
Amount = [[9,8,7,6,5,4,3,2,1], [11,12,13,14,15,16,17,18,19]]
MaxRow = len(Amount)
Total = 0
for Row in range(0, MaxRow):
    RowTotal = 0
    for Column in range(0, 9):
        RowTotal = RowTotal + Amount[Row][Column]
    print("Total for Row ", Row, " is ", RowTotal)
    Total = Total + RowTotal
print("The grand total is ", Total)


# >> ---------------------- << iteration | do while >>
'''
REPEAT
    OUTPUT "Please enter the password"
    INPUT Password
UNTIL Password = "Secret"
'''
while True:
    Password = input("Please enter the password: ")
    if Password == "Secret":
        break

# >> ------------------------- << iteration | while >>
'''
WHILE Number > 9 DO
    Number ← Number - 9
ENDWHILE
'''
Number = 12
while Number > 9:
    Number = Number - 9
print(Number)

# >> --------------------------------- << procedure >>
'''
PROCEDURE DefaultLine
    CALL LINE(60)
ENDPROCEDURE

PROCEDURE Line(Size : INTEGER)
    DECLARE Length : INTEGER
    FOR Length ← 1 TO Size
        OUTPUT '-'
    NEXT Length
ENDPROCEDURE

IF MySize = Default
    THEN
        CALL DefaultLine
    ELSE
        CALL Line(MySize)
    ENDIF
'''

def DefaultLine():
    Line(60)

def Line(Size):
    Length = 0
    for Length in range(1, Size):
        print('-')

MySize = 3
Default = 60
if MySize == Default:
    DefaultLine()
else:
    Line(MySize)


# >> ---------------------------------- << function >>
'''
FUNCTION SumSquare(Number1:INTEGER, Number2:INTEGER) RETURNS INTEGER
    RETURN Number1 * Number1 + Number2 * Number2
ENDFUNCTION

OUTPUT "Sum of squares = ", SumSquare(10, 20)
'''
def SumSquare(Number1, Number2):
    return Number1 * Number1 + Number2 * Number2

Number1 = 5
Number2 = 10
print(SumSquare(Number1, Number2))


# >> ----------------------------- << file handling >>
'''
DECLARE LineOfText : STRING
OPENFILE FileA.txt FOR READ
OPENFILE FileB.txt FOR WRITE
READFILE FileA.txt, LineOfText
WRITEFILE FileB.txt, LineOfText
CLOSEFILE FileA.txt
CLOSEFILE FileB.txt
'''
LineOfText = ""
FileA = open("data/FileA.txt", 'r')
FileB = open("data/FileB.txt", 'w')
LineOfText = FileA.read()
FileB.write(LineOfText)
FileA.close()
FileB.close()