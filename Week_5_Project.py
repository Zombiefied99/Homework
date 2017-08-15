print ("Welcome Fools.")
raw_input('Press enter to continue: ')
print ("Behold the Scars of Mirrodin.")
name = raw_input("Enter name: ")
print(name)
print("I understand that your name is Steve. Is that right?")
print(" Type y for Yes n for No. ")

def n():
    return No

def y():
    return yes

def w():
    return w

def t():
    return Thief

def k():
    return Knight

def n():
    return North

def w():
    return West

def e():
    return East

def s():
    return south
# I think def was all worthless code
x = raw_input('y or n: ')
if x != "n":
    print("Alright Steve your adventure starts here!")
else:
    print("Alright Steve your adventure starts here!")
    
raw_input('Press enter to continue: ')

print(" First you must choose a class. What would you like to be? Type w for Wizard, k for Knight, or t for Thief.")
c = raw_input('w,k,t: ')
if c == "w":
        print (""" You chose the Mighty Wizard!
              _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/ """)
elif c == "k":
            print (""" You chose Boastful Knight!
           
              .
             /.\
             |.|
             |.|
             |.|
             |.|   ,'`.
             |.|  ;\  /:
             |.| /  \/  \
             |.|<.<_\/_>,>
             |.| \`.::,'/
             |.|,'.'||'/.
          ,-'|.|.`.____,'`.
        ,' .`|.| `.____,;/ \
       ,'=-.`|.|\ .   \ |,':
      /_   :)|.|.`.___:,:,'|.
     (  `-:;\|.|.`.)  |.`-':,\
     /.   /  ;.:--'   |    | ,`.
    / _>-'._.'-'.     |.   |' / )._
   :.'    ((.__;/     |    |._ /__ `.___
   `.>._.-' |)=(      |.   ;  '--.._,`-.`.
            ',--'`-._ | _,:          `='`'
            /_`-. `..`:'/_.\
           :__``--..\\_/_..:
           |  ``--..,:;\__.|
           |`--..__/:;  :__|
           `._____:-;_,':__;
            |:'    /::'  `|
            |,---.:  :,-'`;
            : __  )  ;__,'\
            \' ,`/   \__  :
            :. |,:   :  `./
            | `| |   |   |:
            |  | |   |   ||
            |  | |   |   ||
            |  | |   '   ||
            |  : |    \  ||
            |  ; :    :  ||
            | / ,;    |\,'`.
            ;-.(,'    '-._,-`.
          ,'-.//          `--' 
          `---' """)

else:
            c=="t"
            print (""" You chose the Sneaky Thief?
       ,.                 .,
         ,: ':.    .,.    .:' :,
         ,',   '.:'   ':.'   ,',
         : '.  '         '  .' :
         ', : '           ' : ,'
         '.' .,:,.   .,:,. '.'
          ,:    V '. .' V    :,
         ,:        / '        :,
         ,:                   :,
          ,:       =:=       :,
           ,: ,     :     , :,
            :' ',.,' ',.,:' ':
           :'      ':WW::'   '.
          .:'       '::::'   ':
          ,:        '::::'    :,
          :'         ':::'    ':
         ,:           ':''     :.
        .:'             '.     ',.
       ,:'               ''     '.
       .:'               .',    ':
      .:'               .'.,     :
      .:                .,''     :
      ::                .,''    ,:
      ::              .,'','   .:'
    .,::'.           .,','     ::::.
  .:'     ',.       ,:,       ,WWWWW,
  :'        :       :W:'     :WWWWWWW,          .,.
  :         ',      WWW      WWWWWWWWW          '::,
  '.         ',     WWW     :WWWWWWWWW            '::,
   '.         :     WWW     :WWWWWWWW'             :::
    '.       ,:     WWW     :WWWWWWW'             .:::
     '.     .W:     WWW     :WWWWWW'           .,:::'
      '.   :WW:     WWW     :WWWWW'      .,,:::::''
     .,'   ''::     :W:     :WWWWW.  .,::::''
  ,'        ''','',',','','''WWWWW::::''
   ':,,,,,,,':  :  : : :  :  :WWWW''' """)
            print (" A cat is close enough. Do you agree?")
            x = raw_input('y or n: ')
            if x == 'n':
                    print(" I honeslty dont care what you think because you chose a cat. ")
            else:
                    print (" Great minds think alike! ")

raw_input('Press enter to continue: ')

print (" You awaken from a deep slumber. ")
print (" You notice that you're in a cabin. ")
print (" Next to you is a weapon on the ground. ")

raw_input('Press enter to continue: ')

if c == 't' :
    print (" You pick up your dagger. ")
elif c == 'w' :
    print (" You pick up your wand and fake beard. ")
else:
    c == 'k' 
    print (" You pick up your sword and shield. ")
    
print(" You walk outside into the thick forest. Which direction would you like to walk? North, West, East, or South? ")

d = raw_input(' n,w,e,s: ')
while True:
    if (not (d == 'n' or d == 'e' or d == 'w' or d == 's')):
        d == raw_input(' n,w,e,s: ')
    else:
        if d == 'n':
            print (" You walk north until you run into a giant stone wall. ")

            raw_input('Press enter to continue: ')
            
            print (' "Halt, who goes there?" You look up to see an Stormcloak Guard. ')
            break
        elif d == 'w':
            if c == 't':
                print (" You see a goblin in the brush up ahead and then turn around going back to the cabin. ")
                print (" Make wiser decsions. ")
            elif c == 'k':
                print (" You walked into a goblin but you were able to slay it before it could kill you. Then you head back to the cabin. ")
                print (" Make wiser decsions. ")
            else:
                c == 'w'
                print (" You were unable to cast your spell in time. It stabbed you 76 times, then ate you for dinner ")
                print (" Congrats, you achievd ending D. You died in the shortest amount of time. ")
                quit()
        elif d == 'e':
            print (" The forest is getting thicker but you run into a huge, crumbling wall. ")
            print (' "Halt, who goes there?" ')
                       
            raw_input('Press enter to continue: ')
                       
            print (" You look around to see an Imperial Guard. ")
            break
        else:
            d = 's'
            print (" You walk upon a shore and can not continue any further. You turn around and head back to the cabin.  ")
            print (" Make wiser decsions. ")
        d = raw_input(' n,w,e,s: ')
       
raw_input('Press enter to continue: ')

if d == 'e':
       print (''' "Quick, you must follow me. It's not safe here." the guard said. ''')
       print (" Would you like to ask what happend here? ")
       x = raw_input('y or n: ')
       if x == 'y':
           raw_input('Press enter to continue: ')
       else:
           print (" What happend here? ")
           print (" We have been at war with the Imperials for over 20 years, and it just keeps looking worse and worse for us. ")
else:
        d == 'n'
        print (' "What are you, stupid? Get in here before those barberic Stormcloaks attack again." said the guard. ')

print(" Come, tis policy that you meet our Jarl. ")

raw_input('Press enter to continue: ')

print(" You enter a castle, and the first thing you see is the stunning chandler hanging over a table filled with sweetrolls. Behind the table is the Jarl himself sitting upon his throne. ")
print(' "Sir Arthur, who is this fool standing in front of me?" said the Jarl. ')

raw_input('Press enter to continue: ')

print(' "I found this person outside the gate, my lord Jarl Balgruuf of Snowdin." ')
print(" The Jarl stares at you while drinking from a coconut. ")

raw_input('Press enter to continue: ')
print(" Wait a minute, would you like to ask how he got the coconut? ")

x = raw_input('y or n: ')
if x != 'y':
    raw_input('Press enter to continue: ')
else:
    print (" Wait a minute Jarl, how did you get that coconut? ")
    print (' "We found it on the ground. Why does it even matter?" ')
    
    raw_input('Press enter to continue: ')
    
    print(" Well, becuase this is a temperate zone and coconuts are a tropical fruit. ")
    print(' "Pidgeys may fly south with the sun or the sparrows. Even indegious rocks may seek warmer climates and yet these are not strangers to our land?!" ')

    raw_input('Press enter to continue: ')

    print(" Jarl, are you telling me Coconuts migrate ")

    raw_input('Press enter to continue: ')

    print(' "Not at all." ')
    print(' "They could be carried by a pidgey." Arthur joined in. ')

    raw_input('Press enter to continue: ')

    print('"What, a pidgey carring a coconut?" ')
    print(' "It can grasp the coconut by the husk." ')

    raw_input('Press enter to continue: ')
    
    print(" It's not a question about where it grasps the coconut, but a simple question about weight ratio. A 5 ounce bird can not carry a 1 pound coconut!!!! ")
    print(' "Watch who you are talking to with that kind of attutide. I am still the Jarl." ')

    raw_input('Press enter to continue: ')

print(""" "If you are willing I have a tribe of goblins in the west from here. Why don't you kill them to prove your worthy of my time?" """) 
print(' "You can even have my Knight Sir Arthur at your command." ')

raw_input('Press enter to continue: ')

print(' "But, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but, but I dont want to." ')
print(' "No more buts from you, now go!" ')
print(' "Awwwww" groaned Steve and Arthur. ')

raw_input('Press enter to continue: ')

print(" You and Arthur traval day and night to the tribe. You are about 10 meters out from the goblin tribe. ")
print(' "Okay, how do you want to attack? At night or when the sun breaks?" ')
m = raw_input('night or day: ')
if m == 'night':
    print(' "Okay, we will rest up, at midnight we will attack." ')
    print(" Hey Arthur, what's going on down there. The tribe is making a lot of noise. ")

    raw_input('Press enter to continue: ')
    
    print(' "By the beard! Its a goblin rave party." ')
    print(" Well, how are we suppose to get in now? ")
    print(' "The only way in now is through the bouncer and he has a list." ')

    raw_input('Press enter to continue: ')

    print(" Just follow my lead Arthur. ")
    print(" You two wait in the line for what seems like a decade, but now it's your turn. ")

    raw_input('Press enter to continue: ')
    
    print("""

          ,      ,
            /(.-""-.)\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\
      /       '----'       \

    "It looks like you guys are not on the LIST!" """)
    # All of the ascii art are messed up
    if c == 'w':
        print(" Well, look again. You were able to make the names appear on the list. ")
    elif c == 'k':
        print(' "Come at me bro!!!" You yell at the bouncer. ')
        print(' "This will be your last mistake humon." ')
        raw_input('Press enter to continue: ')
        print(" The Goblin comes chargeing at you. ")
        print(" You have to dodge to the right or the left. ")
        raw_input('r or l: ')
        if raw_input == 'r':
            print(" You grab him by the shoulder blades. While digging your fingers into his skins, you change his monmentum to run head first into the hut behind you. ")
        else:
            print(" Dodging to the left, you trip him to send him hurling towards the ground. As he was falling you jumped into the air landing on his back with all the force you had. ")
        print(' "Now that his LIST is gone, we can all PPPPPPPPPPPAAAAAAAAAAAAAAAAAAAAAARRRRRTTTTTTTTTTTTTTTTTTTTYYYYYYYYY!!!!" yelled the crowd ')
    else:
        c == 't'
        print(""" You appear right behind him. Then whisper into his ear "I'm steve". """)
        print(""" Listen you litte freak, you better let us pass before I Kill you, your family, friends, and make you watch me as I kill Shawna. """)

        raw_input('Press enter to continue: ')

        print(' "How do you know about my fiance?" ')
        print(" Remember, I'm Steve the thief, NOT the cat. ")
        
        raw_input('Press enter to continue: ')

        print(' "You guys can pass." ')

    print(' "Well, that went smoothly" said Arthur ')
    print(" Now What do we do? ")
    raw_input('Press enter to continue: ')
    print(" It would be a waste not to party. Wouldn't it? ")
    s == raw_input('y or n: ')
    if s == 'y':
        print(" Hey Arhtur, why don't we take a break and party? ")
        raw_input('Press enter to continue: ')
        print(" You and Arthur spend the night partying with the goblins. ")
        print(' "Great, now how are we supposed to kill them?" ')
        raw_input('Press enter to continue: ')
        if c == 'w':
                print(" I'll start a fire then we can head back. You can kill the ones that escape. ")
        elif c == 'k':
                print(" I'll challage this entrie village to fight and behead them all!! you roar. ")
        elif c == 't':
                print(" I'm going to poison their livestock and their drinking water. ")
    s == 'n'
    if c == 'w':
        print(" I can make this night last for eternity. We can kill them when they are exhausted. ")
    elif c == 'k':
        print(" While dancing, I'm going to hit them and slowly kill them. ")
    else:
                c == 't'
                print(" Cover your ears, Im going to spit some fire so hot that it's going to make their heads explode. ")
else:
    raw_input == 'day'
    print(" Woah, what happend here? It looks like they had a party. ")
    print(' "Well, it makes our job easier if their too tired to fight back." ')
    if c == 'k':
        print(" That's the coward's way out Arthur, watch me. Wake up and fight me losers. ")
        print(' "I thought this was gonna be easy too." ')
    elif c == 't':
        print(" I'm going to start a war with another goblin tribe to frame them. ")
    else:
        c == 'w'
        print(" Im calling down a bunch of meteors to give them radiation poisoning. ")
        
raw_input('Press enter to continue: ')
print(' "That was the most inhumane way I saw somebody kill things." ')
print(" Now that things are done here, we can go back. Right, Arthur? ")
raw_input('Press enter to continue: ')
print(" While you and Arthur are heading back you hear screams of terror and agony behind you. ")
print(" Arthur is laughing at the screams of agony while you are leaving. ")
print(" You arvive at the Jarl's house agian. ")

raw_input('Press enter to continue: ')

print(' "Well, how did he do Arthur?" ')
print(""" "He'll do just fine for your next task, my lord." """)
if d == 'n':
    print(' "Great, next if your up for it Steve, there is an ancient artifact east of here ccapable of destorying those Stormcloaks once and for all." ')
else:
    print(' "Great, next if your up for it Steve there is an ancient artifact east of here capable of destorying those Imperials once and for all." ')
print(' "And I want you to retrieve it for me." ')

raw_input('Press enter to continue: ')

print(" If that is your will. But how do I find it? ")
print(' "It will be in a chest, deep in a cave to the east. Now leave." ')

raw_input('Press enter to continue: ')

print(" You travel east only to find a cave that is so short you could see the end of it from the opening. ")
raw_input('Press enter to continue: ')
print(""" "Yo John, what's with the crappy ending?" said Adam. """)
print(""" "Im sorry dude, but I got tired last night and didn't have enough time to finish it. Anyway dude, just keep playing it.  You're ruining the game with all these questions! """)
raw_input('Press enter to continue: ')
print(" You enter the incredibly short cave to find the chest. ")
print(" A strange hermit stops you. ")
raw_input('Press enter to continue: ')
print(' "Listen you, the Jarl has been tricking you ever since you woke up!" said the hermit. ')
print(" Would you like to listen to what the hermit has to say? ")
x = raw_input('y or n: ')
if x == 'y':
    print(' "He is actually an Orclord that has put you in a spell over you. Changing your perspective. Everything, even those so called goblins, are not real. My family died because you killed them.  Now I want revenge for them!!" ')
else:
    print(" Your wrong about everything old man. ")
raw_input('Press enter to continue: ')
print(" Now get out of the way old man. ")
print(" You open the chest anyways, only to find a rock. ")
raw_input('Press enter to continue: ')
print(" You bring it back to the Jarl. ")
print(' "So did you find it?" ')
raw_input('Press enter to continue: ')
print(" Yes but it was only a rock. ")
print(""" "I can't believe you found it. Quick, hand it over to me." """)
raw_input('Press enter to continue: ')
print(" Would you like to hand over the rock or kill him with it? ")
r = raw_input(' kill or hand: ')
if r == 'kill':
        if c == 'w':
            print(" You pulled out your wand and zapped Sir Arthur with a lightning bolt frying him on the spot. Then you cast a fireball at the Jarl turning him into ash. ")
        elif c == 'k':    
            print(" You beat Sir Arthur's head in with the rock. Then you turn around and threw the rock with all your strength sending the rock right through his chest. You went to retrieve your rock.")
        else:
            print(" You hand over a decoy rock that explodes in his face as you slit open Sir Arthur's neck. ")
else:
        print(""" "Now that I have the rock I can finally end the humans' pathetic lives!" """)
        print(' "But lord, what do we do with Steve now?" ')
        raw_input('Press enter to continue: ')
        print(' "Go ahead and cast him out." ')
        print(" You are cast out into the forest, only to be greeted by a guard. ")
        raw_input('Press enter to continue: ')
        print(' "Stop you piece of garbage. You have commited crimes againest the Scars and her people. What say you in your defense?." ')
        print(" Would you like to resist or go peace fully? ")
        raw_input('Press enter to continue: ')
        k = raw_input('peace or resist: ')
        if k == 'resist':
                    print(" Im not going down without a fight sucker! ")
                    print(" As you turn around the guard grabs you and shoves his sword through your back. ")
                    print(" Congrats, you acheived ending D. You almost made it but now you are dead. ")
                    quit()
        else:
                    print(" After 30 years of jail you were relased back into society. ")
                    print(" You took an arrow in the knee, so you gave up adventuring. ")
                    raw_input('Press enter to continue: ')
                    print(" You marry a nice elf who broke the curse on you. Then you had a kid. ")
                    name = raw_input('Enter name for kid : ')
                    raw_input('Press enter to continue: ')
                    print(name,' Grew up to be an adventurer just like you! ')
                    print("Congrats, you achieved ending C. Not bad, but you could have done better. At least you are not dead. ")
                    quit()
                    
print(" Behind the wall you notice a hole that looks like the rock can fit into. ")
print(" You place the rock in the hole and hear a small door opening to your left. You take a peak to see what is inside the hidden door and find stacks of gold! ")
raw_input('Press enter to continue: ')
print(" You take all the gold, drink a potion labeled antidote, and exit the Orc camp. ")
print(" You live out the rest of your life, rich and alone. THE END.")
print(" Congrats, you achevied ending B. You are alive and rich. That is about as good as it gets.  ")
raw_input('Press enter to continue: ')
print(' "Wait a minute John, how do you get an A ending?" ')
print(""" "Oh dude, that's easy. You just don't play the game!" """)
quit()
