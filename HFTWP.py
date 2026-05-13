"""This is a quiz program about hunt for the wilderpeople. By Caleb M 8th of May 2026"""
#Seting up variables and lists
import time
import os
os.system('cls')
quesorde = 0
orde = ["0","1","2","3","4","5","6","7","8","9"]
opt = [1, 2, 3, 4]
awnse = 0
score = 0
#Questions and answers
ques = {
    "All of the following characters are in the film except..." : 4,
    "Who did Ricky name his dog after?" : 1,
    "What animal killed Zag" : 2,
    "Who can't read or write?" : 1,
    "What does Bella put in ricky's bed to cheer him up?" : 2,
    "How many household did ricky go trough?" : 4,
    "How many dogs died in the film?" : 2,
    "How many cats appeared in the film?" : 1,
    "Can ricky drive a car?" : 2,
    "What is Rickys favorite type of poem" : 3
}
awns = [
    "1: Ricky Baker\n2: Bella Faulkner\n3: Paula Hall\n4: Trisha Smith", 
    "1: Tupac Shakur\n2: John Wick\n3: Mortron\n4: Zig",
    "1: A tic\n2: A boar\n3: A snake\n4: A hunter", 
    "1: Uncle Hec\n2: Psyco Sam\n3: Ricky Baker\n4: Kahu", 
    "1: A bear trap \n2: A hot water bottle\n3: An apple\n4: A car", 
    "1: 1\n2: 2\n3: 3\n4: Too many to count", 
    "1: 0\n2: 1\n3: 2\n4: 3", 
    "1: 0\n2: 1\n3: 2\n4: 3",
    "1: No\n2: Yes\n3: It wasn't in the movie\n4: Maybe",
    "1: Sonnets\n2: Acrostic\n3: Haikus\n4: He doesn't like poems."
]
#Asking the questions in the quiz
for i in ques:
    os.system('cls')
    print(i)
    print(awns[quesorde])
    try:    
        awnse = int(input(""))
    except:
#testing for non interger answers
        while awnse not in opt:
            try:
                os.system('cls')
                print("Invalid input. Please input 1, 2, 3 or 4. 2")
                print("")
                print(i)
                print(awns[quesorde])
                awnse = int(input(""))
            except:
                continue
    if awnse != ques[i]:
#testing for boundry breaking answers
        if awnse > 4 or awnse < 1:
            while awnse not in opt:
                try:
                    os.system('cls')
                    print("Invalid input. Please input 1, 2, 3 or 4. 1")
                    print("")
                    print(i)
                    print(awns[quesorde])
                    awnse = int(input(""))
                except:
                    continue
    if awnse == ques[i]:
        print("Correct!")
        score = score + 1
        print(score)
        quesorde = quesorde + 1
        time.sleep(2)
    else:
        print(f"Incorrect... The awnser was {ques[i]}")
        quesorde = quesorde + 1
        time.sleep(2)
#Final score resault
finalsc = score * 10
if finalsc < 3:
    print(f"Did you watch the movie? \nYou only got {finalsc}% of the questions correct.")
elif finalsc < 8:
    print(f"You got {finalsc}% of the questions correct!")
else:
    print(f"Wow you got {finalsc}% correct! \nWell done.")