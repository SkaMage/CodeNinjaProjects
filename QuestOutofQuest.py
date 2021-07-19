def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (L or R)")
    
    answer = input(">").lower()
    
    if "l" in answer:
       vampireRoom()
    elif "r" in answer:
        slimeRoom()
    else:
        gameOver("You really cant type can you? all you had to do was press l or r. now die") 

def gameOver(reason):
    print("\n" + reason)
    print("Game Over!")

def vampireRoom():
    print("\nBefore you lies a coffin that is closed and 2 windows behind it")
    print("Do you want to open the coffin(1) or ignore it(2) or open the window(3)?")
    
    answer = input(">").lower()
    
    if answer == "1":
        gameOver("A vampire rises out of the coffin pulls out a gun and shoots you right in the face")
    elif answer == "2":
        gameOver("You walk around the coffin and the last thing you hear is a creaking then a gunshot")
    elif answer == "3":
        print("You walk to the window and throw it open. ") 
        print("Sunlight streams into the room and the coffin opens to reveal a passage and an extra crispy vampire")
        skeletonRoom()
    else:
        gameOver("You didnt choose one of the options so the penalty is death")

def slimeRoom():
    print("\nYou walk into a circular room with a large pool in the center.")
    print(" The pool is filled with a red jelly like substance at the bottom of which there is a key")
    print(" Do you dive into the jelly(1) or eat the jelly(2)?")
    
    answer = input(">").lower()
    
    if answer == "1":
        gameOver("You dive into the jelly and find its very hard to swim in things that are not fluid and you drown.")
    elif answer == "2":
        print("You start eating the jelly and it tastes like... jello?")
        print("After retrieving the key you unlock the door and proceed through")
        skeletonRoom()
    else:
        gameOver("You have failed to press 1 or 2. Your incompetence is astounding. now die")

def skeletonRoom():
    print("\nYou enter a room with a large skeleton sitting on a throne.")
    print(" As you approach it lifts its head and says 'NYAHAHA I AM SKELTOR BY WHAT POWER DO YOU APPROACH MEEEEEEEE?????' ")
    print("Do you reply 'BY THE POWER OF GREYSKULL!!!!!!'(1), 'HEEEYYYYYYEAHHHHHHHHYYYEAAAHHHHHYEAAAHHHYEAAHHHH'(2), 'Whats goin on?'(3)")
    
    answer = input(">").lower()
    
    if answer == "1":
        print("'HE MAN?!?!?! NOOOOOOOOOOOOOOO'")
        print("You take out the Power Sword and smite Skeletor where he stands.")
        powerSword()
    elif answer == "2":
        print("You belt out some beautiful lines of verse and Skeletor is so overwhelmed by your powerful voice he faints")
        powerOfSong()
    elif answer == "3":
        print("'Honestly its been such a long time since anyone has asked thank you'")
        print("Skeletor smiles kindly at you and shows you the way forward")
        powerOfFriendship()
    else:
        gameOver("1.2..3... HE'S DOWN")

def powerSword():
    print("\nAs the skeleton crumbles under the might of your sword a path appears in the stone ahead of you.")
    print("As you walk down the path it splits left and right. From the right you see a faint glow, from the left you smell oil and grilling meat")
    print(" Which path do you take? left(1) or right(2)")
    
    answer = input(">").lower()
    
    if answer == "1":
        gameOver("you walk down the tunnel and it gets brighter and brighter. Eventually you come into a large room filled with lava. As you see no way forward the you turn to find you path has been sealed and the lava is rising. As the lava reaches you, all you can think is 'I smell delicious'")
    elif answer == "2":
        mcDonalds()
    else:
        gameOver("(Gilbert Gotfried voice) You Fool!!! now die")

def powerOfSong():
    print("\n.As you step over the passed out skeleton you notice two doors labeled 'XF' and 'AI'")
    print("Which door do you take? XF or AI?")
    
    answer = input(">").lower()
    
    if answer == "xf":
        xFactor()
    elif answer == "ai":
        gameOver("You open the door and walk onto the stage of Americal Idol! Americas SweetHeart Ryan Seacrest sneaks up behind you, cuts out your eye, and sticks it in a creepy doll. The last thing you hear is 'THIS.... is American eyedoll'")
    else:
        gameOver("Cmon you really couldnt press two letters consecutively properly? now die")

def powerOfFriendship():
    print("\nThe way forward is dark, damp, and definitely dirty.")
    print("As you start forward you notice Skeletor look down dejectedly.")
    print("Do you invite him along with you(1) or continue on your way cause skeletons can't have facial expressions! They dont even have any muscles!(2)")
    
    answer = input(">").lower()
    
    if answer == "1":
        print("Alas I cannot accompany you good friend but remember this. The answer is 42")
        mcDonalds()
    elif answer == "2":
        print("You hear a soft sobbing behind you as you walk away and down the hall")
        mcDonalds()
        
    else:
        gameOver("At least you weren't soulless and picked option 2... now die")   
 
def xFactor():
    print("\nYou open the door to the stage of The X Factor and see the horrifying visage of Simon Cowell. He sneers down at you from his spot atop an enormous X.")
    print(" He raises one eyebrow in a questioning manner.")
    print(" Do you begin singing to the best of your ability?(1) Make a dash for the gap in the bottom of the X?(2) or Compliment Simon on his success as an indivdual and impressive eyebrow game?(3)")
    
    answer = input(">").lower()
    
    if answer == "1":
        gameOver("You serenade Simon with your best rendition of Silent Night and he looks to you and says 'Is that it? Thats the best you've got?' And like each word was an arrow piercing your heart you keel over dead.")         
    elif answer == "2":
        print("You make a mad dash and dive underneath the X and begin falling down a sloping tunnel.") 
        endGame()    
    elif answer == "3":
        gameOver("'You cant win me over with petty compliments. Simon says DIE!'")   
    else:
        gameOver("Sorry Dawg you just aint got that xFactor")

def mcDonalds():
    print("\nFollowing your nose you wander your way into a Micky D's and immediatly begin craving a Big Mac.")
    print("There is a counter and a single employee behind the counter.")
    print("Do you order a Big Mac at the register?(1) or Go to the bathroom first?(2)")
    
    answer = input(">").lower()
    
    if answer == "1":
        print("You order a Big Mac and the satisfaction of a well earned sandwhich brings you to enlightnment")
        endGame()
    elif answer == "2":
        gameOver("You smell the bathroom before entering but against better judgement you still enter. Before you is a horror scene the likes of which you brain cannot comprehend. Like a void of swirling unending mess with its epicenter in a toilet. Your mind breaks and you cease to be who you were.")        
    else:
        gameOver("Really you got this far and had a typo? Thats rough buddy. Now die")

def endGame():
    print("\nYou find yourself in a pure white room with a single console in the center.")
    print("On the console are buttons numbered 0-9")
    print("You hear a voice boom out and ask 'What is the answer?'")
    
    answer = input(">").lower()
    
    if answer == "42":
        print("A pearly white gate opens ahead of you and you can tell paradise awaits on the other side")
    else:
        gameOver("Incorrect. And you were so close too. Try being a bit nicer this time? Now die")

start()
