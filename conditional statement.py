print("result for student")
while(True):
    EnterScores = int(input("Enter your score :"))
    #print("your score is ", EnterScores)
    if EnterScores >69:
        stored = ("A")
        print(stored)
    elif EnterScores >59:
        stored = ("B")
        print(stored)
    elif EnterScores>49:
        print("C")
    else:
        print("F")
