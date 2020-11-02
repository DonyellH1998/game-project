import sys
import time
import msvcrt as m

#To make sure sentences stay more or less the same length throughout the game
#   slowprint('“Ugh, I feel like my head just went into a rollercoaster that was going into a blender that’s using a ')
#           slowprint('“Ugh, I feel like my head just went into a rollercoaster that was going into a blender that’s using a ')   
def slowprint(s):
    #Used to print text slowly
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./35)

def wait():
    #Waits for key to be pressed to continue text
    m.getch()

def start():
    
    slowprint('\nAs you come too, you’re awaken by rumbling and beeping sounds all over you. As you look around you, ')
    slowprint('you see that you’re flying an airplane. It’s a one-seater, but you realize that instead of flying ')
    slowprint('straight or up, you’re diving straight down, and one of your wings is on fire. But, for some reason, ')
    slowprint('you feel composed and relaxed, and you’re thinking straight.')

def surv_choice_to_do():
    
    slowprint('\nWhat would you like to do???:')
    slowprint('- Look around inside the plane\n- Look outside the plane\n- Try steering the plane\n- Close your eyes\n')

def surv_what_to_do():
    
    choice = input('Answer: ').lower()
    while choice != 'look around inside the plane':
        if choice == 'look outside the plane':
            slowprint('The first thing you see is the wing of the plane is on fire, black smoke is coming ')
            slowprint('out of a propeller. As you look down, you see a big, blue ocean. Then you realize that ')
            slowprint('you are still going down, and that you don’t have time to gaze at the big, blue ocean, ')
            slowprint('even though it’s very beautiful. ') 
            surv_choice_to_do()
            choice = input('Answer: ').lower()
        elif choice == 'try steering the plane':
            slowprint('You grab hold of the steering wheel, and you turn it left and right like you’re ')
            slowprint('playing and arcade flight simulator, and you’re making the “woosh” and “brrrt” sound ')
            slowprint('that people do when they’re fake flying a plane that is shooting guns. After doing that, ')
            slowprint('you realize that the steering wheel isn’t working anymore.') 
            surv_choice_to_do()
            choice = input('Answer: ').lower()
        elif choice == 'close your eyes':
            slowprint('You close your eyes hoping that when you open it, you’re either safe on a fluffy bed ')
            slowprint('watching a movie on an 85-inch television, or that you’re in a classroom, doing a math quiz. ')
            slowprint('Actually, you thought about it, and you rather be in the burning plane than in a classroom. ')
            slowprint('When you open your eyes, you’re still in the burning plane.') 
            surv_choice_to_do()
            choice = input('Answer: ').lower()
        else:
            slowprint('Choose one of the answers listed above!')
            surv_choice_to_do()
            choice = input('Answer: ').lower()

    if choice == 'look around inside the plane':
        slowprint('As you look around, you see that every light in front of you is blinking red, and you deduct')
        slowprint('that your plane is failing due to your wing being on fire. On your left, you see a cup ')
        slowprint('holder, with a can of Dountain Mew. On your left, you see a lever, and on top of the lever, is ')
        slowprint('a blinking sign that says “EJECT”.')

def surv_choice_to_do2():
    
    slowprint('\nWhat would you like to do???:')
    slowprint('- Take a nice dip in the ocean\n- Scream for help\n- Check your chair\n')

def surv_what_to_do2():
    
    choice = input('Answer: ').lower()
    while choice != 'check your chair':
        if choice == 'take a nice dip in the ocean':
            slowprint('You gaze at the ocean. It’s nice and blue, and you think of going for a swim. ')
            slowprint('But then you thought “I don’t really have a dryer to dry your clothes, or even ')
            slowprint('worse, you don’t have an extra pair of underwear” and you decide not to take a ')
            slowprint('swim in the ocean, even though it looks amazing.') 
            surv_choice_to_do2()
            choice = input('Answer: ').lower()
        elif choice == 'scream for help':
            slowprint('You want to check if you’re alone on the island, but at the same time, you kind of don’t ')
            slowprint('want to know if you’re not alone on the island. The habitants on the island could be civilized ')
            slowprint('people or aliens... ')
            slowprint('What? You never know.') 
            surv_choice_to_do2()
            choice = input('Answer: ').lower()
        else:
            slowprint('Choose one of the answers listed above!')
            surv_choice_to_do2()
            choice = input('Answer: ').lower()

    if choice == 'check your chair':
        slowprint('You go back to your chair and see if you can find anything on it. You see on the back of ')
        slowprint('the chair, there’s a pouch, conveniently containing a machete, and a small bag. Inside the ')
        slowprint('bag is a zippo lighter and a small journal.')   

#Main function that calls all survival functions in this module
def survival_portal():
    
    #Starting point
    start()

    surv_choice_to_do()

    surv_what_to_do()

    slowprint('Your only option is to pull the “EJECT” lever. You make sure your seatbelt is fastened, and that you’re ')
    slowprint('mentally and physically ready for what’s about to happen next. \n')

    slowprint('As you pull the lever, the hatch you’re in opens, and you’re launched out of the plane. You feel the rush ')
    slowprint('of cold air from the outside on your face. As you start to fall (because that’s how gravity works), a ')
    slowprint('parachute deploys behind your chair, and you start to float down. \n')

    slowprint('Conveniently, as you float down, you float towards an island in the middle of the ocean. You feel like ')
    slowprint('that this was “supposed” to happen. But at the same time, you just think that you had a stroke of luck. \n')

    slowprint('As you get closer to the island, you realize that you’re about to land on a white sand beach. As you land ')
    slowprint('(surprisingly smooth, you thought), you take of your seatbelt and look around you. As you saw earlier, ')
    slowprint('you are on a white sand beach.')

    surv_choice_to_do2()

    surv_what_to_do2()