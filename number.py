#guess a number btwn 1-9
import random

chances=5
# number guesser func will generate the number and give user 5 chences
def numberGuesser(num):
        randomNo=random.randint(1,9)
        global chances
        print(randomNo)
        if(num==randomNo):
            print("your guess is ok")
        elif(num>randomNo):
            print("your guess is high , guess a lower no")
        elif(num<randomNo):
            print("your guess is low , guess a higher no")
        chances=chances-1
        print(chances)

#to ask again for number
while(chances>0):
    w=int(input("enter the number: "))
    print(type(w))
    numberGuesser(w)
    
if(chances==0):
    print("your chances are over")    
    
   


