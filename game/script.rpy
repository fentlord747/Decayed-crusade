# Declare characters used by this game. The color argument colorizes the
# name of the character.
define n = Character(' ')
define pov = Character("[povname]", color="#FAFA33")
define L1 = Character("Lucus", color="#a1aced")
define L2 = Character("Lucus Rivera", color="#a1aced")
define Rad = Character("unknown man", color="#8f8f8f")
define k = Character("Kid", color="#c20078")
define a1 = Character("Aiden", color="#b7e8a9")
define a2 = Character("Aiden Thomas", color="#b7e8a9")
define tka = 0

#ASSETS FILES
#BackGrounds
image bg bus = "bussy cover.jpeg"
image bg Funkys = "Custom .jpeg"
image bg Hradio = "Hradio.jpg"
image bg Hes = "hes.jpg"

#Characters 
image drive = "Driver.png"
image mc = "Funny horse.png"
image tounge = "Tounge.png"
image madh = "Mad horse.png"
image tank = "Tank top horse.png"

# if tka >= 1:
#     jump tka_end

# The game starts here.

#Find where this was suposed to go
transform half_size: 
    zoom .5 #adjust as required to scale the images 

transform slide_right:#Slides the called image to the right
    linear 0.5 xpos 0.65

transform slide_left:#Slides the called image to the left
    linear -0.05 xpos -0.5

label start:
  
    $ povname = renpy.input("What is your name?", length=32) # used to ask for name
    $ povname = povname.strip()


    if not povname:
        $ povname = "John"
    
    if povname.lower() == "adolf hitler":
        jump special

    if povname.lower() == "juno":
        jump juno

    "Your name is [povname]."
    jump game_start

label game_start:
    play music "bus engine.wav" volume 0.5

    
    scene bg Funkys
    
    "Lucas Rivera in his bus driver outfit looks over to you. Being friends with him since childhood, he looks at you holding the radio."

    L1 "Hey [povname] what are you up-to?"
    
    show bg bus
    show mc:
        xpos 0.3
        ypos 0.17

    pov "Nothing much, man. just gonna checking if theres anying being broadcastedon the radio."
    
    scene bg Hradio

    menu:
        "Tune left":
            jump tune_left
        
        "Tune Right":
            jump tune_right

label tune_left:
    scene bg bus
    
    Rad "ATTENTION ATTENTION ALL LIVING AND CONCIOUS NEW YORKERS, A SAFE LOCATION HAS BEEN SECURED IN VAN CORTLANDT PARK. THERE IS FOOD, SHELTER, AND WATER."

    show tounge:
        xpos 0.3
        ypos 0.3

    menu:
        "We have to check it out":
            jump check_it
        "think it's real?":
            jump Real

label check_it:
    
    hide tounge
    
    show drive:
        xpos 0.3
        ypos 0.17
    L1 "You sure my guy Can we trust them?"
    hide drive
    show tank:
        xpos 0.3
        ypos 0.17
    pov  "We have to. Aint no way we're not going."
    pov "You heard it loud and clear. We can't miss an oppotunity like this!"
    hide tank
    show drive:
        xpos 0.3
        ypos 0.17
    L1 "I'm not sure man "
    hide drive

    
    pov "You sure my guy? You're telling me there's no curiosity in that head of yours?"
    
    hide tank

    show bg Hes
 
    "Hesitation looms over you, something about it is intriguing but is it worth checking?"
    
    hide bg Hes
    show bg bus
    menu:

        "Nah not really":
            jump nah
        "Fuck it we out":
            jump f1

label nah:
    # Player chooses not to check it out  take a reasonable default action.
    L1 "Alright. We keep moving then."
    jump watch

label Real:
    L1 "It has to be. They wouldn't do something like this, and so clear like that."
    "Maybe it was the way he was talking but he's confident in himself right now which is new. Maybe this is a new start. Something good."
    pov "Fuck it we out"
    jump f1

label f1:
    L1 "Thats what i'm talking about man this will be great. We can't go far right now but we've got about half an hour before the sun sets. we can get to the next gas station for sure"
    "You look out and the sun in almost close to setting. A fog in the distance as your hear Lucas setting up the bus. He seems happy like this."

    menu:
        "Stand with him":
            jump standw
        "Keep watch in the back":
            jump watch

label standw:
    "You lean beside the door of the booth and look forward. The hum of the engine loud and clear, the view dimming as the sun is setting. Turning towards the brooklyn navy yard, you hear a scream."
    # Add some different text effect
    L1 "What the fuck was that?"
    pov "I don't know man"
    L1 "Think we should check it out?"

    menu:
        "Let's Check it out":
            jump check2
        "Let's leave it alone":
            jump leave2

label leave2:
    L1 "Maybe it's nothing. We should keep moving."
    # You can branch this further if you like; for now go back to watching/drive.
    jump watch

label check2:
    pov "Hold up we gotta stop."
    "The bus comes to a hard stop. The sound of rubber wheels skidding on the cracked pavement."
    L1 "The sun looks low man we don't got much time"
    "Lucas looks at you, gas mask in hand, are you sure?"
    "You grab the gas mask and say follow me"

    menu:
        "Go left":
            jump left2
        "Go right":
            jump right2

label left2:
    "The cries get louder, it echoes through the vacant streets. Each step getting closer to the sound. Turning the corner, you see a boy in tears."
    "Wearing torn patched clothes, dirt on his face with messy hair and a slim stature. He looks to be no older than 10. With little time before the sun fully sets,"
    "you pick him up. Rushing back to the familiar bus, the driver is set on your distance. Opening the door and swift to close it."

    pov "What's your name kid?"
    k "its Aiden Thomas but you can call me Aiden"
    pov "Nice to meet you Aiden. The guy up front that drives the bus is Lucas. I'm [povname]"
    pov "Are you hungry Aiden?"
    "As you ask a loud grumble can be heard coming from his stomach as he nods."

    menu:
        "Give him your ration for the day":
            jump givef
        "We have food. Take as much as you need":
            jump spoil

label spoil:
    "Lucas looks over at you, glee in his face as he leans back in his chair. You sit, still watching the kid before noticing he's just staring at the food."

    menu:
        "Help":
            jump tka_end
        "Relax and rest":
            jump tka_end

label givef:
    "You lean down beside your stash of belongings, the kid stands beside you."
    "As you dig in you can see the kid trying to peek over you."
    "You pull out a can."

    menu:
        "Hand him the can":
            jump canc
        "Open the can first":
            jump cano

label canc:
    pov "Enjoy kid"
    "The kid stares at you lost."
    "He reaches but stops."
    pov "Are you gonna take the can or not?"
    "He grabs the can and continues to stare at you with that lost look again."
    pov "oh what are you TOO good for my Chef BOYARDEE beef ravloil little orphan boy"
    pov "Gimme that can"
    "as you reach for the can he says no its not open"
    pov "oh"

    menu:
        "My bad let me open it":
            jump cano
        "Than say something sooner":
            jump canass

label cano:
    pov "Here's the food"
    a1 "Thank you [pov]"
    pov "Where are your parents?"
    a1 "I got separated from my mom in the smoke"
    pov "well Aiden we can help you look for your mom"
    a1 "really you will"
    pov "yep but first we need to go somewhere else rn"

    menu:
        "Continue":
            jump tka_end

label canass:
    pov "How am I supposed to know, speak up kid"
    "You reach for the can and open it up for the kid."
    pov "Here you go oliver"
    a1 "oliver?"
    pov "Nothing don't worry, anyways where are your parents?"
    a1 "oh well I got separated from my mom in the smoke"
    pov "well Aiden we can help you look for your mom"
    a1 "really you will"
    pov "yep but first we need to go somewhere else rn"

    menu:
        "Continue":
            jump tka_end

label right2:
    "As you both run out of the bus you make a right."
    pov "Shit I don't hear them anymore"
    "You can feel the air slowly thicken, your eyes begin to burn. You begin to realize that your mask isn't working."
    pov "We gott... cough... cough... back"
    "You run back toward the bus holding your breath, eyes burning."
    "You see Lucus running past you hitting the Officer Earl Run. He gets to the bus first and opens the door."
    L1 "Hurry up and get in [povname]"
    "You leap for the bus doors and fall into the buss, behind the door shuts swiftly and tight."
    L1 "Are you dumb or are you stupid"
    pov "What if they were in danger"
    L1 "well you almost died trying lets get out of here and get the gas we need"

    # Make sure You add the end of chapter flag
    menu:
        "No child":
            jump Noc

label Noc:
    # Handle the 'No child' branch (placeholder)
    a1 "No child? then let's keep moving and find supplies."
    jump tka_end

label watch:
    "Sitting by the rations, you watch the outside. There's about 15 minutes left in the day before you have to stop somewhere."
    "The noise of the bus is loud and shakes with cracks in the road. Making the turn up towards the brooklyn navy yard, a cry inching closer."

    L1 "What the fuck was that?"

    menu:
        "I don't, let's check the engine?":
            jump check1
        "Ignore it and keep going":
            jump leave1

label check1:
    pov "Stop the bus Lucus. we gotta check the sound."
    "The bus stops. Lucus looks at you, you sure you wanna check it out now?"
    "You walk to the front of the bus and put your mask on, before walking outside to inspect the engine."
    "Story still in progress thanks for playing"
    jump tka_end

label leave1:
    "You look at Lucus AHH we should be fine."
    # Add big white flash and boom effect (placeholder text)
    "You hear an extremely loud bang and a bright flash."
    jump tka_end

label tune_right:

    "Slowly moving the nob right, a voice can barely be heard over the already spotty sound of"
    Rad "ATTENTION ----- ALL ---- NEW YOR --- SAFE LOC--- HAS BEEN SECURED IN VAN CORT  ----- ARK. THERE IS ----  SHEL -------"
    "Lucas looks over, concern still on his face"
    L1 "van cortlandt? thats mad deep. you think it's real?"

    menu:
        "Of course it is":
            jump real
            
        "Let's wait and see if they broadcast again'":
            jump wait

label real:
    pov "they have to be. there is no way they'd be stupid enough to not be deadass about this."
    L1 "i dont know man they could be. what if they do what they do in those movies where they like bomb big places."
    
    menu:
        "No dude we should go":
            jump wsg

        "Lets wait it out":
            jump wait
label wsg:
    "he looks at you and takes a deep breath. Anger hinting at you behind his eyes. "
label wait:
    "with a sigh, you think for a second. Together you could be doing so much more, getting somewhere better or at least a head start to something new."
    a1 "alright whatever. your decision."
    jump tka_end



    menu:
        "Ask again":
            jump aa
        
        "listen and wait":
            jump law

label aa:
    a1 "you positive we should wait it out? you're not curious like at all? bro we haven't heard anything in the past two years. we could be out of this shit." 
    pov "I think we should wait it out. we just don't know. let's sleep on it."

    menu:
        "Listen and wait":
            jump law
        "Try again":
            jump ta 

label ta: 
    pov "come on lucas. This could be our last chance at this thing. We could use this. i know we're not too hot on fuel but we can pick some up on the way easy. You never know. this could be real. I say we do this."
    "with baited breath he sighs..."
    L1 "alright you got me. Let's just be quick."

label law:
    "the sun slowly descending in the background, lucas boarding up the doors and secondary exits. Focused on your tasks, you divide up the rations you both have managed to save. Somewhat low but not like it wouldn't last a couple of days. Between the both of you, there is definitely food for a night or two."
    
    menu:
        "Talk to Lucas":
            jump tlk2l
        
        "Sleep off the night":
            jump slpnig

label tlk2l:
    "You sit beside where his booth is. He's settled and looking forward, avoiding eye contact with you."
    L1 "we're not doing too good on fuel. We stop for gas every day. I don't mean to be all nervous but we can't be making rash decisions all the time."
    L1 "I wanna be on the safe side, not get us into trouble. If we see anyone you think is chill, we can bring them on... but it'll be on you if they fuck us up."
menu:
    "We will be good":
        jump wbg
    
    "No promises":
        jump nprm


label wbg:
    "He shakes his head side to side with his arms already crossed. Leaning back in his chair and placing his cap over his face, a big exhale before a soft snore emits from him."

    menu:
        "Check rations":
            jump chckr

        "Sleep":
            jump sleep

label chckr:
    "In the back, a small bodega crate sits in front of you, tied down to the seat and a makeshift cover made of cut up pallet planks on top accompanied by a lock. Pulling out the key from a hidden compartment in the air vent of the bus, You open it."
    "4 cans. That could last you 2 days. There's food to spare for now."

    jump sleep

label nprm:

l1 "when is there ever."
'leaning back in his chair and placing his cap over his face, he settles in for the night. Soft snores emit from him. Now alone with your thoughts, what could you do?'
menu:
    "Sleep":
        jump sleep

    "Check rations":
        jump chckr
        
label sleep:
    "Finally resting in your usual spot in the back of the bus by the rations, you lay for a second, the divots in the seats uncomfortable against your back but you've been getting used to it. You think to yourself"
    pov "We just have to make it there." 

    menu: 
        "wake up":
            jump wakup1


label wakup1:

    "The alarm set beside you vibrates, you had taken out the speaker long ago in the beginning.  Eyes slightly blurry, you rub them and make your vision clear. "
    "You look over to Lucas who is preparing a bag for the day. Eating the first half of his can of the day."
     
    L1 "So you ready for this? We have a day ahead of us."

    menu:
        "Yea lets get to it":
            jump tka_end
        
        "Should we check outside first?":
            jump tka_end
        
        

label special:

    "If you picked [povname] congrats you unlocked a super secert ending "
    "|| | |_ |_| enjoy I hope you get it"
    jump tka_end
label juno:
    "Esto no tiene ningún significado, es solo una broma. Usé el traductor de Google"
    jump game_start












label tka_end:
    "Thank you for playing this super dooopper epic epic game 
        if your game ended abruptly you have reached the end of said arc."
    return