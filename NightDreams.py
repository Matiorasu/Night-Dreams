import random
import time

# signals the end of the game, whether the player is caught or escapes
# used in the while loop
end = 0
# signals whether the player was caught
badEnd = 0
# signals whether the player was successful
goodEnd = 0
# message delay timer as provided by the user
delay = 0
# determines whether the player has confirmed their preferred delay time.
delayConfirm = "false"
# validDelay determines if the delay entered is an integer
validDelay = "false"
# title screen

'''
Multi-line comment
'''

#intro screen, comment out for testing
print("Welcome, player, to... whatever this is.")
time.sleep(3)
print("If you enjoy this demo, do let me know on Twitter or Youtube.")
time.sleep(3)
print("But first, I want to help make you more comfortable.")
time.sleep(3)
print("You may have noticed there's a slight, deliberate delay between these messages.")
time.sleep(4)
print("These are used to help control the pacing for people who need a moment to read.")
time.sleep(4)
print("But, some of you may not like the delay very much at all.")
time.sleep(3)
print("So, if you please. Tell me how long, in seconds, you want to be allowed read these messages.")
time.sleep(5)

print("Enter your choice now.")

while (delayConfirm != "true"):
    delay = int(input())
    delay = str(delay)

    print("You want the delay to be " + delay + " seconds. (true/false)")
    
    delayConfirm = str(input())
    delay = int(delay)
    if (delayConfirm != "true"):
        print("Let's try that again. Input the length, in seconds, of time you want to be allowed to read incoming messages.")

print("Wonderful!")
time.sleep(delay)
print("Now, let's get on with our story.")




def sniper(difficulty):

    #diagnostic print
    print(difficulty)

    sniperPhase = 0
    sniperEnd = "false"

    while (sniperEnd != "true"): 
        time.sleep(15)
        sniperMove = random.randint(0,difficulty)

        #diagnostic print
        print(sniperMove)

        if (sniperMove > 5):
         sniperPhase += 1
         if (sniperPhase == 1):
            print("The sniper has arrived.")
         elif (sniperPhase ==2):
            print("The sniper is taking aim.")
         elif (sniperPhase == 3):
            print("The sniper has killed the player.")
            sniperEnd = "true"


#while loop for the sniper activation


#while (1==1):
 #   sniper(11)


def thatcher(difficulty):

    #diagnostic print
    print(difficulty)

    #thatcher should arrive at the end of the full time of the day
    time.sleep(5)
    thatcherDelay = random.randint(0,15)

    #diagnostic print
    print(thatcherDelay)

    thatcherArrival = thatcherDelay - difficulty

    #diagnostic print
    print(thatcherArrival)

    time.sleep(thatcherArrival)
    if(playerKill == "false"):
        print("Thatcher catches the player, gives them a demerit.")
    else:
        print("Thatcher kills player.")



#thatcher can simply be called with the current difficulty
#remember, thatcher still needs to know whether to kill the player

#thatcher(11)


def police(difficulty):

    policePhase = 0
    policeEnd = "false"

    #diagnostic print
    print(difficulty)

    #the police should wait for a brief moment to arrive.
    initialDelay = random.randint(30,60)
    trueDelay = initialDelay - (difficulty*2)
    time.sleep(trueDelay)
    while (policeEnd == "false"):
        time.sleep(30)
        policeMove = random.randint(0, difficulty)

        #diagnostic print
        print(policeMove)

        if (policeMove > 5):
            policePhase += 1

            if (policePhase == 1):
                print("Police have arrived.")
            if (policePhase == 2):
                 print("The Police are monitoring the player")
            if (policePhase == 3):
                print("The police have arrested the player.")
                policeEnd = "true"

police(15)