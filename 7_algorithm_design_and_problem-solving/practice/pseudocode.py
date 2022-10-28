import random

# >> ------------------------------------ << arrays >>
'''
DECLARE StudentNames : ARRAY[1:30] OF STRING
StudentNames ← "Ali"
StudentNames[n+1] ← StudentNames[n]

DECLARE NoughtsAndCrosses[1:3, 1:3] OF CHAR
NoughtsAndCrosses[2,3] ← 'X'
'''


# >> --------------------- << arithmetic operations >>
'''
Bits ← 2 ^ 5
AnswerOne ← DIV(10, 3) returns 3
AnswerTwo ← MOD(10, 3) returns 1
'''


# >> -------------- << logical & boolean operations >>
'''
IF Answer < 0 OR Answer > 100 AND Answer != 50
    THEN
        Correct ← FALSE
    ELSE
        Correct ← TRUE
ENDIF
'''


# >> ------------------------- << string operations >>
'''
LENGTH("Happy Days" will return 10)
LCASE('W') will return 'w'
UCASE("Happy") will return "HAPPY"
SUBSTRING("Happy Days", 1, 5) will return "Happy"
'''



# >> --------------------------- << library routnes >>
'''
Value ← ROUND (RANDOM() * 6, 0) // returns whole number between 0 and 6
'''


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


# >> ---------------------- << iteration | do while >>
'''
REPEAT
    OUTPUT "Please enter the password"
    INPUT Password
UNTIL Password = "Secret"
'''


# >> ------------------------- << iteration | while >>
'''
WHILE Number > 9 DO
    Number ← Number - 9
ENDWHILE
'''


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


# >> ---------------------------------- << function >>
'''
FUNCTION SumSquare(Number1:INTEGER, Number2:INTEGER) RETURNS INTEGER
    RETURN Number1 * Number1 + Number2 * Number2
ENDFUNCTION

OUTPUT "Sum of squares = ", SumSquare(10, 20)
'''


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

