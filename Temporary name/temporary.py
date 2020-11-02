import sys
import time
import msvcrt as m

import survival

class PlayerInfo():
    name = ""
    gender = ""
    primarygenre = ""
    secondarygenre = ""

def slowprint(s):
    #Used to print text slowly
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./35)

def wait():
    #Waits for key to be pressed to continue text
    m.getch()

def confirmation_prompt():
    #Confirms with user for their prompt
    answer = ""
    while answer not in ['yes', 'no']:
        answer = input('\nYes or No?: ').lower()
        if answer not in ['yes', 'no']:
            slowprint("\nPlease type 'Yes' or 'No': ")
    return answer

def gender_question():

    gender, answer, player_name = '', '', ''
    while (gender not in ['male','female']) or (answer not in 'yes'):
        print('***************')
        player_name = input('Name: ')
        gender = input('Gender(Male/Female): ').lower()
        print('***************')
        if gender == 'male':
            slowprint(f"\nSo, your name is {player_name.capitalize()}, and you're {gender}... as in a guy, correct???")
            answer = confirmation_prompt()
        elif gender == 'female':
            slowprint(f"\nSo, your name is {player_name.capitalize()}, and you're {gender}... as in a girl, correct???")
            answer = confirmation_prompt()
        else: 
            slowprint("\nPlease answer 'Male' or 'Female': \n")
        #if answer == 'no':
        #    slowprint("\nThen, you better wake up and type the right answer!!!")
    return player_name, gender

def choice_genre(): #Works with only 2 choices 
    #While we don't actually have a confirmation, keep prompting from the list
    answer, choiceisvalid = '', False
    slowprint('\nThen, let us begin...\n')
    slowprint('Wait a sec, one more thing, sorry about that...\n')
    slowprint("Please choose 2 out of the following list, it's not important or anything: ") #Change to 3 later
    slowprint('- Shooter(1st person)\n- Survival(3rd person)') #\n- Racing(Unavailable)\n- Simulation(Unavailable)\n- Sport(Unavailable)\n- Role-Playing(Unavailable)
    #While choices are correct or confirmation isn't yes
    while (answer not in ["yes"]) or (choiceisvalid == True):
        slowprint('\nChoose your 2 genres: ')
        choice1 = input('\nChoose your 1st genre: ').lower()
        choice2 = input('Choose your 2nd genre: ').lower()
        if (choice1 == 'shooter' and choice2 == 'survival' or choice1 == 'survival' and choice2 == 'shooter'):
            slowprint(f'\nYour choices are {choice1} and {choice2}, right???')
            answer = confirmation_prompt()
            if answer == 'yes':
                slowprint('\nThen, let us finally begin...\n')
                return [choice1, choice2]
            elif answer == 'no':
                slowprint('\nThen, you better wake up and choose the correct 2 genres!!!')
        else:
            slowprint('\nPlease put a valid answer from the list!!!')

def choice_to_do():
    
    slowprint('\nWhat would you like to do???:')
    slowprint('- Look around\n- Look at your body\n- Scream your name out loud\n')
    
    return

def what_to_do(gender, player_name):
    
    choice = input('Answer: ').lower()
    while choice != 'look around':
        if choice == 'look at your body':
            if gender == 'male':
                slowprint('While looking at your body, first thing you realize is that you have a gut. Not big enough ')
                slowprint('to be called fat, but not small enough to “not see”. ')
                slowprint('You know what I mean, right? ')
                wait()
                slowprint('Other than that, you’re wearing a blue jumpsuit (which is really tight) and has a ')
                slowprint('yellow light on your chest.')
                wait()
                choice_to_do()
                choice = input('Answer: ').lower()
            elif gender == 'female':
                slowprint('While looking at your body, you realize that you have pretty long hair. Like it reaches ')
                slowprint('your butt. You say to yourself “This length isn’t really suitable for other than ')
                slowprint('making a mess everywhere, aka easy to get a DNA sample of me”.') 
                wait()
                slowprint('Other than that, you’re wearing a blue jumpsuit (which is really tight) and has a ')
                slowprint('yellow light on your chest.')
                wait()
                choice_to_do()
                choice = input('Answer: ').lower()
        elif choice == 'scream your name out loud':
            player = f'“MY NAME IS {player_name}!!!”'
            slowprint(f'{player.upper()}, you scream out loud. Your voice just echoes for a bit, and now you feel ')
            slowprint('kinda stupid for doing that.')
            wait()
            choice_to_do()
            choice = input('Answer: ').lower()          
        else:
            slowprint('Choose one of the answers listed above!')
            choice_to_do()
            choice = input('Answer: ').lower()

    if choice == 'look around':
        slowprint('You look around and you see that there’s only a couple of things. You see four oval things in ')
        slowprint('front of you, three of them are glowing and radiating rainbow-like colors. The first one is ')
        slowprint('just grayed-out though, almost looks like it’s “turned off”.')
        wait()

def choice_to_do2():

    slowprint('\nWhat would you like to do?:')
    slowprint('- Inspect the "glowing signs"\n- Approach a portal\n- Wait around\n')

    return

def what_to_do2(choice1, choice2):
    
    choice = input('Answer: ').lower()
    while choice != 'inspect the "glowing signs"':
        if choice == 'wait around':
            slowprint('You decide to wait until you see someone, or until something happens… ')
            wait()
            slowprint('After exactly 2 minutes and 32 seconds later, you realize that it was 2 minutes and 32 seconds ')
            slowprint('of your life wasted…')
            choice_to_do2()
            choice = input('Answer: ').lower()
        elif choice == 'approach a portal':
            slowprint('You thought to yourself, “Might not be a good idea to just go closer to one of the portals without ')
            slowprint('checking it out first. ')
            wait()
            slowprint('You never know, a huge tentacle might come out and grab me, or even worse, a mandatory surprise math ')
            slowprint('quiz might pop out…" ')
            slowprint('You shiver in fear after the thought of a surprise math quiz.')
            wait() 
            choice_to_do2()
            choice = input('Answer: ').lower()          
        else:
            slowprint('Choose one of the answers listed above!')
            choice_to_do2()
            choice = input('Answer: ').lower()

    if choice == 'inspect the "glowing signs"':
        slowprint('You look more closely to each portal, and you realize that each portal has a different sign on ')
        slowprint(f'them. “{choice1.capitalize()}”, “{choice2.capitalize()}” and “choice3”. ')
        wait()
        slowprint('The portal that seems “turned off”, the sign on top of this portal is blank. You don’t give ')
        slowprint('much attention to that portal, and you return your focus on the other 3 portals.\n')
        wait()

def choice_to_do3(choice1, choice2): #Only 2 options for now

    slowprint('\nThe big question is, which one of the portals do you choose?: ') 
    slowprint(f'- {choice1.capitalize()} portal\n- {choice2.capitalize()} portal\n')#- {choice3} portal\n') 

    return

def what_to_do3():
    
    choice = input('Answer: ').lower()
    if choice == 'survival portal':
        slowprint('Survival portal chosen\n')
        slowprint('Once you enter the portal, your vision suddenly blacks out, but you’re still able to ')
        slowprint('think but you can’t move your body, it’s basically like sleep paralysis. ')
        wait()
        slowprint('You can’t tell how long you’re in this state, but you know one thing for sure, ')
        slowprint('you don’t know what you’re expecting at the other side. ')
        wait()
        survival.survival_portal()
    elif choice == 'shooter portal':
        slowprint('Shooter portal chosen\n')
        slowprint('Once you enter the portal, your vision suddenly blacks out, but you’re still able to ')
        slowprint('think but you can’t move your body, it’s basically like sleep paralysis. ')
        wait()
        slowprint('You can’t tell how long you’re in this state, but you know one thing for sure, ')
        slowprint('you don’t know what you’re expecting at the other side. ')
        wait()
    else:
        slowprint('Choose one of the answers listed above!')
        what_to_do3()
        choice = input('Answer: ').lower()
       
#Runtime

#Player info
player = PlayerInfo()

#Choose gender
player.name, player.gender = gender_question()

#Get genres the player wants
player.primarygenre, player.secondarygenre = choice_genre()
    
#Begin adventure :)
slowprint('“Ugh, I feel like my head just went into a rollercoaster that was going into a blender that’s using a ')
slowprint('V9 engine as a motor” you say as you wake up from possibly being unconscious. ')
wait()
slowprint('You look around, and you don’t really know where you are. Well, you don’t remember anything at all…')
slowprint('You remember the language that you speak though, which is English, well you think it’s English.')
wait()
slowprint(f'\nOnly thing you do remember that matters is your name. “My name is {player.name}”, you say to yourself.')
wait()

choice_to_do()

what_to_do(player.gender, player.name)

slowprint('\nAs you look more closely to the ovals, you realize that they’re some kind of portal. ')
slowprint('These portals are making a weird ominous sound, but at the same time, it looks like ')
slowprint('that’s your only option to get out of wherever you currently are. ')
wait()
slowprint('As you inspect these portals further, you see that on top of each portal, there’s a ')
slowprint('“glowing sign” just hovering above each portal. ')
wait()
slowprint('\nEach sign says something different. ')
wait()

choice_to_do2()

what_to_do2(player.primarygenre, player.secondarygenre)

slowprint('As you see read whatever is on top of the portal, you realize that it kind of sounds familiar, ')
slowprint('but can’t quite put your finger on it. ')
wait()
slowprint('Only option is that you can think of at the moment is to walk into one of these portals. ')
wait()

choice_to_do3(player.primarygenre, player.secondarygenre)

what_to_do3()

input('\nPress ENTER to exit')