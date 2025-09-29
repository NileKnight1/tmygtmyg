default leadertalk = 0

label day2:
    scene black with dissolve
    pause 5.0
    "{cps=20}A new day, a new morning ...{/cps}"
    
    jump d2r1

    return

label d2r1:
    scene bg ubd1
    with pixellate
    pause 1.0
    

    show userkaf n at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            
            show mirror1 with dissolve

            u "{cps=20}I have a weird feeling.{/cps}"


            show mirror1 at hideFade with dissolve
            hide mirror1
            jump d2r1


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2s0
        
    return

label d2k1:
    scene bg kitchen1
    with pixellate
    pause 1.5
    show userkaf n at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tasty.{/cps}"
            jump d2k1

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d2r1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2s0
    

    return    

label d2s0:
    scene bg street1 m with pixellate
    pause 1.0
    show userkaf n at left, showFade
    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2r1

        "Go to the palm tree":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2p1

        "Go to the square":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2q1


    return

label d2q1:
    scene bg square with pixellate
    pause 1.0
    show userkaf c at center, showFade

    u "{cps=20}No one is here.{/cps}"
    menu:
        "Go back":
            show userkaf c at center, hideFade
            hide userkaf c
            pause 1.0
            jump d2s0
        
    return

label d2p1:
    scene bg palm1 with pixellate
    pause 1.0
    show minas n at p1, showFade:
        zoom 0.8
    pause 3.0

    show userkaf h at p2, showFade
    pause 1.0
    show minas h at p1:
        zoom 0.8
    u "{cps=20}Hey Minas, too early !{/cps}"
    m "{cps=20}Yeah{/cps}"
    u "{cps=20}I'm not used to that.{/cps}"
    m "{cps=20}THANK YOU!{/cps}"

    show eya h at p3, showFade
    show tausert h at p4, showFade

    pause 1.0
    u "{cps=20}Oh you came together.{/cps}"
    t "{cps=20}Yeah we found out that we live near eachother.{/cps}"
    
    e "{cps=20}Hey boys.{/cps}"
    
    show userkaf b at p2
    m "{cps=20}Hey Eya.{/cps}"
    u "{cps=20}Hey.{/cps}"
    t "{cps=20}Hey.{/cps}"
    m "{cps=20}Hey.{/cps}"
    show userkaf h at p2

    menu:
        "Say 'Anyone particpated before?'":
            u "{cps=20}Anyone particpated before?{/cps}"
            e "{cps=20}Not me.{/cps}"
            t "{cps=20}Same.{/cps}"
            u "{cps=20}Same for us.{/cps}"
            e "{cps=20}I know someone.{/cps}"
        "Say 'We have to find someone who particpated before.'":
            u "{cps=20}We have to find someone who particpated before.{/cps}"
            e "{cps=20}I already know someone.{/cps}"

    u "{cps=20}Great who's she?{/cps}"
    show userkaf n at p2
    e "{cps=20}He's called Intef.{/cps}"
    m "{cps=20}Let's visit him then ...{/cps}"
    m "{cps=20}Where does he live?{/cps}"
    e "{cps=20}On the edges of the village.{/cps}"
    t "{cps=20}Let's go.{/cps}"

    show minas h at p1, hideFade with dissolve:
        zoom 0.8

    show userkaf n at p2, hideFade with dissolve
    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide minas h
    hide userkaf n
    hide eya h
    hide tausert h

    pause 1.5

    jump d2s1

    return

label d2s1:
    scene bg street1 m with pixellate
    pause 1.0


    show minas h at p1:
        zoom 0.8
    show userkaf n at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade

    pause 1.0

    t "{cps=20}The way is too long.{/cps}"
    menu:
        "Say 'Let's rest here.'":
            $ leadertalk = 1
        "Say 'We shouldn't waste time.'":
            pause 1.0
            show minas h at p1, hideFade with dissolve:
                zoom 0.8
            show userkaf n at p2, hideFade with dissolve
            show eya h at p3, hideFade with dissolve
            show tausert h at p4, hideFade with dissolve
            hide minas h
            hide userkaf n
            hide eya h
            hide tausert h
            pause 1.0
            jump intaf
            

    u "{cps=20}Let's rest here.{/cps}"
    m "{cps=20}What's wrong Userkaf?{/cps}"
    u "{cps=20}What?{/cps}"
    m "{cps=20}You look weird.{/cps}"
    u "{cps=20}Nah.{/cps}"
    
    call leaderChat
    u "{cps=20}Let's continue.{/cps}"

    pause 1.0

    show minas h at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf n at p2, hideFade with dissolve
    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide minas h
    hide userkaf n
    hide eya h
    hide tausert h

    pause 1.0

    jump intaf

    return

label intaf:
    scene house intaf m with pixellate
    pause 1.0

    show minas h at p1, showFade:
        zoom 0.8
    show userkaf h at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade
    pause 1.5

    show userkaf n at p2

    i "{cps=20}Hi Eyaaa.{/cps}"
    e "{cps=20}Hey Intaaaf.{/cps}"
    i "{cps=20}Hello guys.{/cps}"
    m "{cps=20}Hey bro.{/cps}"
    t "{cps=20}Hey.{/cps}"
    pause 2.0
    u "{cps=20}Hello.{/cps}"
    e "{cps=20}We wanted to ask you some questions.{/cps}"
    i "{cps=20}Yeah sure go on.{/cps}"
    m "{cps=20}How many time have you particpated in the Guardians of the Nile?{/cps}"
    i "{cps=20}Only once ... The last year.{/cps}"
    t "{cps=20}And this year?{/cps}"
    i "{cps=20}I'm 19, I can't.{/cps}"
    e "{cps=20}We want more details about the contest.{/cps}"
    i "{cps=20}Sure Leader.{/cps}"
    menu:
        "Say 'I'm the leader.'":
            u "{cps=20}I'm the leader.{/cps}"
            i "{cps=20}Aha ...{/cps}"
        "Say 'She's a great leader indeed'":
            u "{cps=20}She's a great leader indeed.{/cps}"
            i "{cps=20}Of course.{/cps}"

    i "{cps=20}Anyways, it goes for 3 days.{/cps}"
    i "{cps=20}First day contains archery contest, wrestling, stick fighting ...{/cps}"
    i "{cps=20}Second day contains senet, mehen and hounds and jackals ...{/cps}"
    i "{cps=20}Last day is for running and boat racing.{/cps}"
    i "{cps=20}Every version has a moral you should learn.{/cps}"
    e "{cps=20}Thank you very much Intaf we really apprecite that.{/cps}"
    t "{cps=20}Thanks Intaf!{/cps}"
    pause 1.0

    menu:
        "Thank him":
            u "{cps=20}Thank you.{/cps}"
            i "{cps=20}You're welcome guys.{/cps}"
        "Skip him":
            i "{cps=20}You're welcome guys.{/cps}"
            i "{cps=20}And good luck CAPTIN CHARISMA.{/cps}"
            u "{cps=20}Me? {nw}{/cps}"
            u "{cps=20}I'm charismatic no doubt.{/cps}"

    u "{cps=20}Okay let's go back.{/cps}"

    pause 1.0

    show minas h at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf n at p2, hideFade with dissolve
    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide minas h
    hide userkaf h
    hide eya h
    hide tausert h

    pause 1.0
    if leadertalk == 1:
        jump d2s2
    else:
        jump d2s22

    return

label d2s2:
    scene bg street1 e with pixellate
    pause 1.0


    show minas h at p1:
        zoom 0.8
    show userkaf n at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade

    pause 1.0

    t "{cps=20}It's almost evening ...{/cps}"
    t "{cps=20}Let's separate now and meet together.{/cps}"
    e "{cps=20}Yeah, we should be home before night.{/cps}"
    u "{cps=20}Okay well.{/cps}"
    e "{cps=20}See you.{/cps}"
    pause 1.0

    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide eya h
    hide tausert h
    pause 1.0

    show minas n at p1:
        zoom 0.8
    m "{cps=20}Brooo!{/cps}"  
    u "{cps=20}Huh?{/cps}"  
    m "{cps=20}You're not good.{/cps}"  
    u "{cps=20}I AM ...{/cps}"  
    u "{cps=20}I told you, don't worry.{/cps}"  
    m "{cps=20}Okay, see you tomorrow.{/cps}"  
    m "{cps=20}Bye.{/cps}"  
    
    pause 1.0

    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    hide minas n

    pause 3.0

    show userkaf s at p2

    pause 5.0

    menu:
        "Go home":
            show userkaf s at p2, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d2r22

        "Go to the palm tree":
            show userkaf s at p2, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d2p2

    return 

label leaderChat:
    e "{cps=20}Bruh I wished to be the leader.{/cps}"
    m "{cps=20}Me too for real.{/cps}"
    t "{cps=20}It doesn't matter actually, it's just a name.{/cps}"
    u "{cps=20}Yeah really, I don't care.{/cps}"
    e "{cps=20}Give me the lead then haha.{/cps}"
    show userkaf h at p2
    u "{cps=20}Why not!{/cps}"
    show userkaf n at p2

    m "{cps=20}She'll be the best leader.{/cps}"
    e "{cps=20}OH, thank you.{/cps}"
    show eya h at p3

    return
    

label d2s22:
    scene bg street1 m with pixellate
    pause 1.0

    show minas h at p1:
        zoom 0.8
    show userkaf n at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade

    pause 1.0
    t "{cps=20}Oh it's still morning.{/cps}"
    u "{cps=20}Yeah because we didn't rest then.{/cps}"
    e "{cps=20}Good job leader.{/cps}"

    menu:
        "Say 'Let's speak here.'":
            u "{cps=20}Let's talk a little.{/cps}"
        "Say 'Let's go to the palm tree.'":
            u "{cps=20}Let's go to the palm tree{/cps}"
            pause 1.0

            show minas h at p1, hideFade with dissolve:
                zoom 0.8
            show userkaf n at p2, hideFade with dissolve
            show eya h at p3, hideFade with dissolve
            show tausert h at p4, hideFade with dissolve
            hide minas h
            hide userkaf h
            hide eya h
            hide tausert h
            jump d2p22

            

    call leaderChat
    pause 1.0
    
    t "{cps=20}I wanna go home.{/cps}" 
    e "{cps=20}Okay, see you later boys.{/cps}" 

    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide eya h
    hide tausert h

    pause 2.0

    show minas n at p1:
        zoom 0.8
    m "{cps=20}Brooo!{/cps}"  
    u "{cps=20}Huh?{/cps}"  
    m "{cps=20}You're not good.{/cps}"  
    u "{cps=20}I AM ...{/cps}"  
    u "{cps=20}I told you, don't worry.{/cps}"  
    m "{cps=20}Okay, see you tomorrow.{/cps}"  
    m "{cps=20}Bye.{/cps}"  
    
    pause 1.0

    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    hide minas n

    pause 3.0

    show userkaf s at p2

    pause 5.0

    menu:
        "Go home":
            show userkaf s at p2, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d2r22

        "Go to the palm tree":
            show userkaf s at p2, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d2p2


    return 

label d2p22:
    scene bg palm1 with pixellate
    pause 1.0

    show minas h at p1:
        zoom 0.8
    show userkaf n at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade

    pause 1.0

    call leaderChat
    t "{cps=20}I wanna go home.{/cps}" 
    e "{cps=20}Okay, see you later boys.{/cps}" 

    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide eya h
    hide tausert h

    show minas n at p1:
        zoom 0.8
    m "{cps=20}Brooo!{/cps}"  
    u "{cps=20}Huh?{/cps}"  
    m "{cps=20}You're not good.{/cps}"  
    u "{cps=20}I AM ...{/cps}"  
    u "{cps=20}I told you, don't worry.{/cps}"  
    m "{cps=20}Okay, see you tomorrow.{/cps}"  
    m "{cps=20}Bye.{/cps}"  
    
    pause 1.0

    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    hide minas n

    pause 3.0

    show userkaf s at p2
    pause 3.0

    menu:
        "Stay here for a while":
            jump d2p2
        "Go away":
            show userkaf s at p2, hideFade
            hide userkaf s
            jump d2s00

    return

label d2s00:
    scene bg street1 e with pixellate
    pause 1.0
    show userkaf s at left, showFade

    menu:
        "Go home":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d2r22
        "Go to the palm tree":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d2p2
        "Go to the square":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d2q2

    return

label d2q2:
    scene bg square2 with pixellate
    pause 1.0
    show userkaf s at center, showFade
    pause 1.0

    u "{cps=20}I need someone to talk with.{/cps}"
    menu:
        "Go back":
            show userkaf s at center, hideFade
            hide userkaf s
            pause 1.0
            jump d2s00
        
    return

label d2r22:
    scene bg ubd2
    with pixellate
    pause 1.0

    show userkaf s at left, showFade
    pause 1.0
    u "{cps=20}No one is home.{/cps}"
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0

            scene bg ubd2 at showBlur
            
            show mirror7 with dissolve

            u "{cps=20}I need someone.{/cps}"


            show mirror7 at hideFade with dissolve
            hide mirror7
            jump d2r22


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            jump d2k22

        "Sleep":
            scene black with dissolve
            pause 1.0
            u "{cps=20}Bruh I can't sleep.{/cps}"
            jump d2r22

        "Go out":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            jump d2s00




    return

label d2k22:
    scene bg kitchen2
    with pixellate
    pause 1.5
    show userkaf s at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tasty.{/cps}"
            jump d2k22

    
        "Go back to your room":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d2r22    

    return    

label d2p2:
    scene bg palm2 with pixellate
    pause 1.0

    show userkaf s at right, showFade
    pause 1.5

    u "{cps=40}WHAT AM I FEELING?{/cps}"
    u "{cps=40}DID I FALL IN LOVE?{/cps}"
    u "{cps=40}how ME loves HER?{/cps}"
    u "{cps=40}SHE'S THE MOST KNOWN GIRL IN THE VILLAGE, EVERYONE KNOWS HER, WHY WOULD SHE CHOOSE ME ON THEM?{/cps}"
    u "{cps=40}I should forget her.{/cps}"

    pause 3.0

    show stranger at left, showFade
    pause 1.0
    ss "{cps=20}I heard some shouting so I came to look.{/cps}"
    ss "{cps=20}Are you okay kid?{/cps}"

    menu:
        "I'm not okay.":
            u "{cps=20}I'm not okay.{/cps}"

    ss "{cps=20}That's love.{/cps}"

    menu:
        "How did you know?":
            u "{cps=20}How did you know?{/cps}"
            ss "{cps=20}I guessed.{/cps}"

    ss "{cps=20}Speak kid, don't bottle it up.{/cps}"

    menu:
        "Speak":
            u "{cps=20}She's in my team.{/cps}"
            ss "{cps=20}Make sense ...{/cps}"
            ss "{cps=20}What's your problem then?{/cps}"
            u "{cps=20}I feel a weird feeling when a boy talks to her.{/cps}"
            ss "{cps=20}That's jealousy.{/cps}"
            ss "{cps=20}It shouldn't be that much.{/cps}"
            u "{cps=20}I don't know how to control it!{/cps}"
            u "{cps=20}PLus, i'm afraid of falling in love.{/cps}"
            ss "{cps=20}But you already did.{/cps}"
            u "{cps=20}NOO.{/cps}"
            ss "{cps=20}You did.{/cps}"
            u "{cps=20}What should I do Mr. Experience.{/cps}"
            ss "{cps=20}The more you give, the more you gain kid.{/cps}"
            ss "{cps=20}Give kindness, care and sympathy ...{/cps}"
            ss "{cps=20}And you'll gain love.{/cps}"


    ss "{cps=20}Do you feel better?{/cps}"
    u "{cps=20}I think ...{/cps}"
    u "{cps=20}I'm going home.{/cps}"
    u "{cps=20}See you later.{/cps}"
    ss "{cps=20}See you soon.{/cps}"

    pause 1.0
    show userkaf s at right, hideFade with dissolve
    hide userkaf s
    pause 1.0

    jump d2r2

    return

label d2s02:
    scene bg street1 n with pixellate
    pause 1.0
    show userkaf n at left, showFade

    menu:
        "Go home":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d2r2
        "Go to the palm tree":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d2p3
        "Go to the square":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d2q3

    return

label d2q3:
    scene bg square3 with pixellate
    pause 1.0
    show userkaf n at center, showFade
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade
            hide userkaf n
            pause 1.0
            jump d2s02
        
    return

label d2p3:
    scene bg palm3 with pixellate
    pause 1.0
    show userkaf n at center, showFade
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade
            hide userkaf n
            pause 1.0
            jump d2s02
        
    return



label d2r2:
    scene bg ubd3
    with pixellate
    pause 1.0

    show userkaf n at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            
            show mirror3 with dissolve

            u "{cps=20}I need some sleep.{/cps}"


            show mirror3 at hideFade with dissolve
            hide mirror3
            jump d2r2


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d2k2

        "Sleep":
            jump day3

        "Go out":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d2s02




    return

label d2k2:
    scene bg kitchen3
    with pixellate
    pause 1.5
    show userkaf n at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tasty.{/cps}"
            jump d2k2

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d2r2    

    return    
