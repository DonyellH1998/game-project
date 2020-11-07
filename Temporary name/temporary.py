import sys
import time
import textwrap
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

def wrap(p):
    #Uses textwrap module to keep sentences printed out to a max of 75
    wrapper = textwrap.TextWrapper(width=90, break_long_words=False, replace_whitespace=False)
    #dedented_text = textwrap.dedent(text=p).strip()
    wrap_list = wrapper.wrap(p)

    for line in wrap_list:
        slowprint(line)

def wait():
    #Waits for key to be pressed to continue text
    m.getch()

def confirmation_prompt():
    #Confirms with user for their prompt
    answer = ""
    while answer not in ['yes', 'no']:
        answer = input('\nYes or No?: ').lower()
        if answer not in ['yes', 'no']:
            wrap("\nPlease type 'Yes' or 'No': ")
    return answer

def gender_question():

    gender, answer, player_name = '', '', ''
    while (gender not in ['male','female']) or (answer not in 'yes'):
        print('***************')
        player_name = input('Name: ')
        gender = input('Gender(Male/Female): ').lower()
        print('***************')
        if gender == 'male':
            wrap(f"\nSo, your name is {player_name.capitalize()}, and you're {gender}... as in a guy, correct???")
            answer = confirmation_prompt()
        elif gender == 'female':
            wrap(f"\nSo, your name is {player_name.capitalize()}, and you're {gender}... as in a girl, correct???")
            answer = confirmation_prompt()
        else: 
            wrap("\nPlease answer 'Male' or 'Female': \n")
        #if answer == 'no':
        #    wrap("\nThen, you better wake up and type the right answer!!!")
    return player_name, gender

def choice_genre(): #Works with only 2 choices 
    #While we don't actually have a confirmation, keep prompting from the list
    answer, choiceisvalid = '', False
    wrap('\nThen, let us begin...\n')
    wrap('Wait a sec, one more thing, sorry about that...\n')
    wrap("Please choose 2 out of the following list, it's not important or anything: ") #Change to 3 later
    wrap('- Shooter(1st person)\n- Survival(3rd person)') #\n- Racing(Unavailable)\n- Simulation(Unavailable)\n- Sport(Unavailable)\n- Role-Playing(Unavailable)
    #While choices are correct or confirmation isn't yes
    while (answer not in ["yes"]) or (choiceisvalid == True):
        wrap('\nChoose your 2 genres: ')
        choice1 = input('\nChoose your 1st genre: ').lower()
        choice2 = input('Choose your 2nd genre: ').lower()
        if (choice1 == 'shooter' and choice2 == 'survival' or choice1 == 'survival' and choice2 == 'shooter'):
            wrap(f'\nYour choices are {choice1} and {choice2}, right???')
            answer = confirmation_prompt()
            if answer == 'yes':
                wrap('\nThen, let us finally begin...')
                return [choice1, choice2]
            elif answer == 'no':
                wrap('\nThen, you better wake up and choose the correct 2 genres!!!')
        else:
            wrap('\nPlease put a valid answer from the list!!!')

def choice_to_do():
    
    wrap('\nWhat would you like to do???:')
    wrap('- Look around\n- Look at your body\n- Scream your name out loud')
    
    return

def what_to_do(gender, player_name):
    
    choice = input('\nAnswer: ').lower()
    while choice != 'look around':
        if choice == 'look at your body':
            if gender == 'male':
                wrap('While looking at your body, the first thing you realize is that you have a gut. Not big enough to be called fat, but not small enough to “not see”. ')
                wrap('You know what I mean, right? ')
                wait()
                wrap('Other than that, you’re wearing a blue jumpsuit (which is really tight) and has a yellow light on your chest.')
                wait()
                choice_to_do()
                choice = input('\nAnswer: ').lower()
            elif gender == 'female':
                wrap('While looking at your body, you realize that you have pretty long hair. Like it reaches your butt. You say to yourself “This length isn’t really suitable for other than making a mess everywhere, aka easy to get a DNA sample of me”.')
                wait()
                wrap('Other than that, you’re wearing a blue jumpsuit (which is really tight) and has a yellow light on your chest.')
                wait()
                choice_to_do()
                choice = input('\nAnswer: ').lower()
        elif choice == 'scream your name out loud':
            player = f'“MY NAME IS {player_name}!!!”'
            wrap(f'{player.upper()}, you scream out loud. Your voice just echoes for a bit, and now you feel kinda stupid for doing that.')
            wait()
            choice_to_do()
            choice = input('\nAnswer: ').lower()          
        else:
            wrap('Choose one of the answers listed above!')
            choice_to_do()
            choice = input('\nAnswer: ').lower()

    if choice == 'look around':
        wrap('You look around and you see that there’s only a couple of things. You see four oval things in front of you, three of them are glowing and radiating rainbow-like colors. The first one is just grayed-out though, almost looks like it’s “turned off”.')
        wait()

def choice_to_do2():

    wrap('\nWhat would you like to do?:')
    wrap('- Inspect the "glowing signs"\n- Approach a portal\n- Wait around')

    return

def what_to_do2(choice1, choice2):
    
    choice = input('\nAnswer: ').lower()
    while choice != 'inspect the "glowing signs"':
        if choice == 'wait around':
            wrap('You decide to wait until you see someone, or until something happens… ')
            wait()
            wrap('After exactly 2 minutes and 32 seconds later, you realize that it was 2 minutes and 32 seconds of your life wasted…')
            choice_to_do2()
            choice = input('\nAnswer: ').lower()
        elif choice == 'approach a portal':
            wrap('You thought to yourself, “Might not be a good idea to just go closer to one of the portals without checking it out first. ')
            wait()
            wrap('You never know, a huge tentacle might come out and grab me, or even worse, a mandatory surprise math quiz might pop out…" ')
            wrap('You shiver in fear after the thought of a surprise math quiz.')
            wait() 
            choice_to_do2()
            choice = input('\nAnswer: ').lower()          
        else:
            wrap('Choose one of the answers listed above!')
            choice_to_do2()
            choice = input('\nAnswer: ').lower()

    if choice == 'inspect the "glowing signs"':
        wrap(f'You look more closely at each portal, and you realize that each portal has a different sign on them. “{choice1.capitalize()}”, “{choice2.capitalize()}” and “choice3”. ')
        wait()
        wrap('The portal that seems “turned off”, the sign on top of this portal is blank. You don’t give much attention to that portal, and you return your focus on the other 3 portals.\n')
        wait()

def choice_to_do3(choice1, choice2): #Only 2 options for now

    wrap('\nThe big question is, which one of the portals do you choose?: ') 
    wrap(f'- {choice1.capitalize()} portal\n- {choice2.capitalize()} portal')#- {choice3} portal') 

    return

def what_to_do3():
    
    choice = input('\nAnswer: ').lower()
    if choice == 'survival portal':
        wrap('Survival portal chosen\n')
        wrap('Once you enter the portal, your vision suddenly blacks out, but you’re still able to think but you can’t move your body, it’s basically like sleep paralysis. ')
        wait()
        wrap('You can’t tell how long you’re in this state, but you know one thing for sure, you don’t know what you’re expecting on the other side. ')
        wait()
        survival.survival_portal()
    elif choice == 'shooter portal':
        wrap('Shooter portal chosen\n')
        wrap('Once you enter the portal, your vision suddenly blacks out, but you’re still able to think but you can’t move your body, it’s basically like sleep paralysis. ')
        wait()
        wrap('You can’t tell how long you’re in this state, but you know one thing for sure, you don’t know what you’re expecting on the other side. ')
        wait()
    else:
        wrap('Choose one of the answers listed above!')
        what_to_do3()
        choice = input('\nAnswer: ').lower()
       
#Runtime

#Player info
player = PlayerInfo()

#Choose gender
player.name, player.gender = gender_question()

#Get genres the player wants
player.primarygenre, player.secondarygenre = choice_genre()
    
#Begin adventure :)
wrap('\n“Ugh, I feel like my head just went into a rollercoaster that was going into a blender that’s using a V9 engine as a motor” you say as you wake up from possibly being unconscious. ')
wait()
wrap('You look around, and you don’t really know where you are. Well, you don’t remember anything at all…')
wrap('You remember the language that you speak though, which is English, well you think it’s English.')
wait()
wrap(f'\nOnly thing you do remember that matters is your name. “My name is {player.name}”, you say to yourself.')
wait()

choice_to_do()

what_to_do(player.gender, player.name)

wrap('\nAs you look more closely to the ovals, you realize that they’re some kind of portal. ')
wrap('These portals are making a weird ominous sound, but at the same time, it looks like that’s your only option to get out of wherever you currently are. ')
wait()
wrap('As you inspect these portals further, you see that on top of each portal, there’s a “glowing sign” just hovering above each portal. ')
wait()
wrap('\nEach sign says something different. ')
wait()

choice_to_do2()

what_to_do2(player.primarygenre, player.secondarygenre)

wrap('As you read whatever is on top of the portal, you realize that it kind of sounds familiar, but can’t quite put your finger on it. ')
wait()
wrap('Only option that you can think of at the moment is to walk into one of these portals. ')
wait()

choice_to_do3(player.primarygenre, player.secondarygenre)

what_to_do3()

input('\nPress ENTER to exit')