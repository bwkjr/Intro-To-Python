import random # For the use of the shuffle function

def Strip(Choice):
    OpenFile = open (Choice, 'r') # opening the file
    x = OpenFile.readlines() #sets value to read all the lines
    seq = []
    for fruit in x:   #this loop creates the sequence of fruits
        seq.append(fruit.strip('\n'))
    return seq   #sends it back to main

def Randomize(seq):
    random.shuffle(seq)     #shuffles the fruits so there are no repeats
    return seq

def Calander (seq, NoD):
    Day = 1
           # had to make a while loop so I could do specific months
    for fruit in seq:    # makes the calander with day next to the fruit
        print ("Day {0} eat this!: {1}".format(Day, fruit))
        Day = Day +1
        if Day == NoD+1:
            break
def Cont():
    yn = input("\nwould you like to return to our menu? ")
    if yn == 'y' or yn == 'Y' :
        print("\n")
        Main()
    else :
        print("\nCYA LATER")
        quit
    
def Main():
    Apples = 'fruitlist2.py' #thought this would be the easiest way to use separate files for the fruits
    Bananas = 'fruitlist.py'
    Squirrels = 'fruitlist3.py'
    NoD = 0
    print("Hello friend. Welcome to The Fruit Stand.\n We Randomley select fruits for you to eat!")   #my friendly menu
    print("We have many varieties of \n Apples \n Bananas \n Squirrels")
    c = input ("What Kind of fruit would you like to eat?(A, B, or S) ")
    if  c == 'A' or c == 'a':     #fun If statements to makes decision based on user input
        seq = Strip(Apples)
    elif c == 'B' or c == 'b':
        seq = Strip (Bananas)
    elif c == 'S' or c == 's' :
        seq = Strip(Squirrels)
    month = input ("For which month would you like to make a randomized list of fruits in that variety? \n(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Nov, Dec)")
        
    if month == 'Apr' or month == 'Jun' or month == 'Sep' or month == 'Nov':    # Used user input to set new value to NoD which is used in the while loop above
        NoD = 30
    elif month == 'Feb':
        NoD = 28
    else:
        NoD = 31
    
    Randomize(seq)      #Call to more functions that do things
    Calander(seq, NoD)
    Cont()
    
    
    
Main()   #Shabam