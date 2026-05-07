"""This is a quiz program about hunt for the wilderpeople. By Caleb M 8th of May 2026"""

import os
os.system('cls')
amo = 0
orde = ["0","1","2","3","4","5","6","7"]
opt = ["1", "2", "3", "4"]
awnse = 0

ques = {
    "All of the following characters are in the film except..." : 4,
    "Who did Ricky name his dog after?" : 1,
    "What animal killed Zag" : 2,
    "Who can't read or write?" : 1,
    "What does Bella put in ricky's bed to cheer him up?" : 2,
    "How many household did ricky go trough?" : 4,
    "How many dogs died in the film?" : 2,
    "How many cats appeared in the film?" : 1
}
awns = [
    "1: Ricky Baker\n2: Bella Faulkner\n3: Paula Hall\n4: Trisha Smith", 
    "1: Tupac Shakur\n2: John Wick\n3: Mortron\n4: Zig",
    "1: A tic\n2: A boar\n3: A snake\n4: A hunter", "1: Uncle Hec\n2: Psyco Sam\n3: Ricky Baker\n4: Kahu", 
    "1: A bear trap \n2: A hot water bottle\n3: An apple\n4: A car", 
    "1: 1\n2: 2\n3: 3\n4: Too many to count", 
    "1: 0\n2: 1\n3: 2\n4: 3", 
    "1: 0\n2: 1\n3: 2\n4: 3"
]

for i in ques:
    print(i)
    print(awns[amo])
    amo += 1
    print(ques[i])
    try:    
        awnse = int(input(""))
    except:

        try:
            print("Invalid input. Please input a number of 1-4.")
            awnse = int(input(""))
        except:
            continue
    if awnse == ques[i]:
        print("Correct!")
    elif awnse != ques[i]:
        if awnse > 4 or awnse < 1:
            print("Invalid input")
        else:
            print("Incorrect...")