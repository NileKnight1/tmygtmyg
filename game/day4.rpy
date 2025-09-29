default temtem = 0
default mfd = 0
default efd = 0
default tfd = 0
default tfdd = 0


label day4:
    scene black with dissolve
    pause 5.0

    jump d4r1

    return

label d4r1:
    scene bg ubd1-2
    with pixellate
    pause 1.0

    show userkaf n at left, showFade
    pause 1.0

    u "{cps=20}...{/cps}"
    u "{cps=20}Oh today is the day ...{/cps}"
    u "{cps=20}So excited.{/cps}"

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd1-2 at showBlur
            
            show mirror5 with dissolve

            u "{cps=20}Weird.{/cps}"


            show mirror5 at hideFade with dissolve
            hide mirror5


            call d4m1


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d4k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4s00

    return

label d4m1:
    scene bg ubd1-2 with pixellate
    pause 1.0
    show userkaf n at left, showFade
    pause 1.5
    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd1-2 at showBlur
            
            show mirror5 with dissolve

            u "{cps=20}Weird.{/cps}"


            show mirror5 at hideFade with dissolve
            hide mirror5


            call d4m1


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d4k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4s00


label d4k1:
    scene bg kitchen1-3
    with pixellate
    pause 1.5
    show userkaf n at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tastes good.{/cps}"
            jump d4k1

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4m1

    return    

label d4s00:
    scene bg street1 m with pixellate
    pause 1.0
    show userkaf n at left, showFade

    menu:
        "Go home":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d4m1
        "Go to the palm tree":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d4p00
        "Go to the square":
            show userkaf n at left, hideFade
            hide userkaf n
            jump d4q1


    return

label d4p00:
    scene bg palm1 with pixellate
    pause 1.0
    show userkaf n at center, showFade
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade
            hide userkaf n
            pause 1.0
            jump d4s00
        

    return

label d4q1:
    scene bg square1-2 with pixellate
    pause 1.0

    show cheif at center, showFade
    pause 1.5
    V "{cps=10}Each team divides itself into two teams.{/cps}"
    V "{cps=10}And come with me.{/cps}"
    pause 1.0
    show cheif at center, hideFade with dissolve
    hide cheif

    pause 1.0
    show minas n at p1, showFade:
        zoom 0.8

    show userkaf n at p2, showFade
    show eya n at p3, showFade
    show tausert n at p4, showFade
    pause 1.0

    t "{cps=20}What why?{/cps}"
    m "{cps=20}Intaf didn't mention that.{/cps}"
    e "{cps=20}I'll choose Minas.{/cps}"

    menu:
        "Keep silence":
            u "{cps=20}...{/cps}"
        "Object":
            u "{cps=20}Why him?{/cps}"
            e "{cps=20}Because he's better than you.{/cps}"
            t "{cps=20}Oh my God.{/cps}"

    t "{cps=20}Okay ... me and Userkaf.{/cps}"
    e "{cps=20}Let's go then.{/cps}"

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

    jump d4s2

    return

label d4s2:
    scene bg street3 with pixellate
    pause 1.0
    
    show userkaf n at left, showFade
    show tausert n at right, showFade
    pause 1.0

    t "{cps=20}Oh look at this temple!{/cps}"
    u "{cps=20}Looks interesting ...{/cps}"
    menu:
        "Say 'Wanna explore it?'":
            u "{cps=20}Wanna explore it?{/cps}"
            t "{cps=20}Mhm ...{/cps}"
            t "{cps=20}And the contest??{/cps}"
            u "{cps=20}We won't be late.{/cps}"
            u "{cps=20}What about Eya and Minas?{/cps}"

            menu:
                "Say 'Leave them.'":
                    u "{cps=20}Leave them.{/cps}"
                    t "{cps=20}Okay let's go.{/cps}"
                    pause 1.0
                    show userkaf h at left, hideFade with dissolve
                    show tausert h at right, hideFade with dissolve
                    hide userkaf h
                    hide tausert h
                    pause 1.0
                    show eya n at left, showFade
                    show minas n at right, showFade:
                        zoom 0.8
                    pause 1.0
                    
                    m "{cps=20}WHERE ARE THEY GOING?!{/cps}"
                    e "{cps=20}They're going to that temple.{/cps}"
                    m "{cps=20}Let's go after them.{/cps}"
                    show eya n at left, hideFade with dissolve
                    show minas n at right, hideFade with dissolve:
                        zoom 0.8
                    hide eya n
                    hide minas n
                    pause 1.0
                    jump d4t1
                    
                "Say 'Call them.'":
                    u "{cps=20}Call them.{/cps}"
                    hide userkaf n
                    hide tausert n
                    show userkaf n at p1, showFade
                    show tausert n at p2, showFade
                    t "{cps=20}EYA MINAS come here.{/cps}"
                    show eya n at p3, showFade
                    show minas n at p4, showFade:
                        zoom 0.8
                    t "{cps=20}We'll explore this temple.{/cps}"
                    e "{cps=20}The contest is goining to start .. We can't now.{/cps}"
                    menu:
                        "Say 'I'm going anyway'":
                            u "{cps=20}I'm going anyway.{/cps}"
                            t "{cps=20}Let's go then.{/cps}"
                            show userkaf n at p1, hideFade
                            show tausert n at p2, hideFade
                            hide tausert n
                            hide userkaf n
                            show eya a at p3
                            show minas a at p4:
                                zoom 0.8
                            pause 2.0
                            jump d4t1

                        "Say 'You're right'":
                            u "{cps=20}You're right.{/cps}"
                            scene black with dissolve
                            jump d4r00

                    


        "Say 'Let's explore it later'":
            t "{cps=20}Okay.{/cps}"
            scene black with dissolve
            jump d4r00


    return


label d4t1:
    scene bg temple1 with pixellate
    pause 1.0

    $ temtem = 1

    show userkaf z at p3, showFade
    show tausert z at p4, showFade
    pause 1.0

    u "{cps=20}Wow.{/cps}"
    t "{cps=20}Facsinating.{/cps}"
    u "{cps=20}I think there's a secret in this place.{/cps}"
    t "{cps=20}Mhm ...{/cps}"

    show minas a at p1, showFade:
        zoom 0.8
    show eya a at p2, showFade

    m "{cps=20}Userkaf !!!{/cps}"
    u "{cps=20}What do you want?!{/cps}"

    scene bg temple2 with pixellate

    show userkaf z at p3 
    show tausert z at p4
    show minas z at p1:
        zoom 0.8
    show eya z at p2
    
    e "{cps=20}Oh my God!{/cps}"
    show minas a at p1:
        zoom 0.8
    m "{cps=20}Are you happy now?{/cps}"
    show eya a at p2
    e "{cps=20}YOU MADE US LOSE USERKAF ...{/cps}"
    e "{cps=20}I HATE YOU.{/cps}"
    show userkaf s at p3

    u "{cps=20}I'm sor—{nw}{/cps}" 
    u "—" nointeract
    show userkaf a at p3 with vpunch
    show minas d at p3:
        zoom 0.8
    show eya z at p1 
    
    m "{cps=20}Don't you speak.{/cps}"
    "Minas pushes Userkaf and falls on ground."

    menu:
        "Kick him":
            show minas z at p2 with vpunch:
                zoom 0.8
            show userkaf d at p3
            "Userkaf kicks Minas.{nw}"
            "—" nointeract
            scene bg temple3 with vpunch
            "The pillar broke. {nw}"
            "—" nointeract

            show userkaf z at p3 
            show tausert z at p4
            show minas z at p2:
                zoom 0.8
            t "{cps=20}IT FELL ON EYA.{/cps}"
            m "{cps=20}YOU MADE US LOSE.{/cps}"
            m "{cps=20}YOU KILLED EYA.{/cps}"
            m "{cps=20}YOU KILLED HER USERKAF.{/cps}"
            jump d4r2
        "Stand up":
            show userkaf d at p3
            menu:
                "Push him":
                    show userkaf d at p3
                    show minas d at p2 with vpunch:
                        zoom 0.8
                    "Userkaf pushes Minas. {nw}"
                    "—" nointeract
                    scene bg temple3 with vpunch
                    "The pillar broke. {nw}"
                    "—" nointeract

                    show userkaf z at p3 
                    show tausert z at p4
                    show minas z at p2:
                        zoom 0.8
                    t "{cps=20}IT FELL ON EYA.{/cps}"
                    m "{cps=20}YOU MADE US LOSE.{/cps}"
                    m "{cps=20}YOU KILLED EYA.{/cps}"
                    m "{cps=20}YOU KILLED HER USERKAF.{/cps}"
                    jump d4r2
                



    return

label d4r2:
    scene bg ubd3 with pixellate

    m "{cps=20}YOU KILLED HER USERKAF.{/cps}"
    um "{cps=20}USERKAF ...{/cps}"
    show umom at left, showFade
    um "{cps=20}Are you okay ?{/cps}"
    show userkaf s at right, showFade
    

    menu:
        "I'm okay.":
            u "{cps=20}I'm okay ...{/cps}"
            u "{cps=20}Just a bad dream.{/cps}"
            
    um "{cps=20}Okay Userkaf ...{/cps}"
    um "{cps=20}I'm here if you need something.{/cps}"
    show umom at left, hideFade with dissolve
    hide umom
    pause 1.5
    show userkaf s at right, hideFade with dissolve
    hide userkaf s
    show userkaf s at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            
            show mirror6 with dissolve

            u "{cps=20}My face is back.{/cps}"


            show mirror6 at hideFade with dissolve
            hide mirror6
            jump d4r3


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            jump d4k2

        "Check Eya's paper":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            
            show expression papyrusN with dissolve

            u "{cps=20}I'm happy that was a dream.{/cps}"


            show expression papyrusN at hideFade with dissolve
            hide expression papyrusN
            jump d4r3

        "Go Out":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d4s3

        "Sleep":
            scene black with dissolve
            pause 1.0
            u "{cps=20}I can't sleep.{/cps}"
            jump d4r3

    return

label d4r00:
    scene bg ubd3 with pixellate
    pause 1.0    

    show userkaf n at left, showFade
    u "{cps=20}Oh it was a dream.{/cps}"

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            
            show mirror3 with dissolve

            u "{cps=20}I wanted to explore that temple.{/cps}"


            show mirror3 at hideFade with dissolve
            hide mirror3
            jump d4r00


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d4k20

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            
            show expression papyrusN with dissolve

            u "{cps=20}I'm happy it's here.{/cps}"


            show expression papyrusN at hideFade with dissolve
            hide expression papyrusN
            jump d4r00

        "Go Out":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4s3
        
        "Sleep":
            scene black with dissolve
            pause 1.0
            u "{cps=20}I can't sleep.{/cps}"
            jump d4r00



    return

label d4k20:
    scene bg kitchen3
    with pixellate
    pause 1.5
    show userkaf n at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tastes real.{/cps}"
            jump d4k20

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4r00
    return    

label d4r3:
    scene bg ubd3 with pixellate
    pause 1.0

    show userkaf s at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            
            show mirror6 with dissolve

            u "{cps=20}I want to vent to someone.{/cps}"


            show mirror6 at hideFade with dissolve
            hide mirror6
            jump d4r3


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            jump d4k2

        "Check Eya's paper":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            
            show expression papyrusN with dissolve

            u "{cps=20}I love this paper.{/cps}"


            show expression papyrusN at hideFade with dissolve
            hide expression papyrusN
            jump d4r3

        "Go Out":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d4s3

        "Sleep":
            scene black with dissolve
            pause 1.0
            u "{cps=20}I can't sleep.{/cps}"
            jump d4r3



    return

label d4k2:
    scene bg kitchen3
    with pixellate
    pause 1.5
    show userkaf s at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tastes real.{/cps}"
            jump d4k2

    
        "Go back to your room":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d4r3

        "Go Out":
            show userkaf s at left, hideFade with dissolve
            hide userkaf s
            pause 1.0
            jump d4s3

    return    

label d4s3:
    scene bg street1 n with pixellate
    pause 1.0

    show userkaf s at left, showFade

    u "{cps=20}I want to talk to the stranger for real.{/cps}" 
    u "{cps=20}I wish he was here.{/cps}" 

    menu:
        "Go back home":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d4r3
        "Go to the palm tree":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d4p1
        "Go to the square":
            show userkaf s at left, hideFade
            hide userkaf s
            jump d4q0

    return

label d4q0:
    scene bg square3 with pixellate
    pause 1.0
    show userkaf s at center, showFade
    pause 1.0

    u "{cps=20}No one is here.{/cps}"
    menu:
        "Go back":
            show userkaf s at center, hideFade
            hide userkaf s
            pause 1.0
            jump d4s3
        
    return



label d4p1:
    scene bg palm3 with pixellate
    pause 1.0

    show userkaf s at right, showFade


    if temtem == 1:
        u "{cps=20}What if this's a sign?{/cps}" 
        u "{cps=20}What if I'll really make them lose.{/cps}"
    pause 2.0
    u "{cps=20}O Allah ...{/cps}"
    u "{cps=20}God of the Nile and the Two Lands ...{/cps}"
    u "{cps=20}Creator of the water and the sands ...{/cps}"
    u "{cps=20}You hear when an human demands ...{/cps}"
    u "{cps=20}And all Your wisdom understands ...{/cps}"
    u "{cps=20}Grant me focus and skills to win the contest ...{/cps}"
    u "{cps=20}And ...{/cps}"
    u "{cps=20}And Eya ...{/cps}"
    u "{cps=20}If she's good for me ...{/cps}"
    u "{cps=20}Bring her near ...{/cps}"
    u "{cps=20}If not ...{/cps}"
    u "{cps=20}Distance her ...{/cps}"
    show userkaf h at right
    pause 3.0
    scene black with dissolve
    pause 5.0

    e "{cps=20}Userkaf ...{/cps}"
    e "{cps=20}Userkaf !{/cps}"
    pause 1.0
    scene bg palm1 with pixellate
    show eya h at left, showFade
    show userkaf b at right, showFade
    e "{cps=20}Good morning.{/cps}"
    
    if temtem == 1:
        menu:
            "Say 'Good morning Eya.'":
                u "{cps=20}Good morning Eya.{/cps}"
            "Ask how she's doing":
                show eya c at left
                u "{cps=20}Eya, are you okay?{/cps}"
                e "{cps=20}Yes.{/cps}"
            "Tell her about the dream":
                show eya c at left
                u "{cps=20}I had a weird dream.{/cps}"
                e "{cps=20}Leave it for later no time left.{/cps}"
    else:
        u "{cps=20}Good morning Eya.{/cps}"


    show eya h at left
    e "{cps=20}Let's go and meet with the rest.{/cps}"
    u "{cps=20}Okay.{/cps}"



    show userkaf h at right, hideFade with dissolve
    hide userkaf h

    show eya h at left, hideFade with dissolve
    hide eya h

    pause 1.0
    jump d4q2

    return

label d4q2:
    scene bg square with pixellate
    pause 1.5

    show minas n at p1, showFade:
        zoom 0.8

    show userkaf h at p2, showFade
    show eya h at p3, showFade
    show tausert n at p4, showFade
    pause 1.0

    m "{cps=20}Where did you find him?{/cps}"
    e "{cps=20}Under the palm tree as I said.{/cps}"
    show tausert h at p4
    show eya b at p3
    t "{cps=20}Perfect leader Eya.{/cps}"
    if leader == 0:
        show userkaf c at p2
        u "{cps=20}Isn't Minas the leader?{/cps}"
        m "{cps=20}I gave her the lead.{/cps}"


    V "{cps=10}Silence.{/cps}"

    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf h at p2, hideFade with dissolve
    show eya b at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide minas n
    hide userkaf h
    hide eya b
    hide tausert h
    pause 1.5

    show cheif at center, showFade
    pause 1.0

    V "{cps=10}As you know {w=0.5} We're celebrating Peret ...{/cps}"
    V "{cps=10}The season of emergence ...{/cps}"
    V "{cps=10}We'll start the day with some shows.{/cps}"
    show cheif at center, hideFade with dissolve
    hide cheif
    pause 1.0
    menu:
        "Speak with them":
            show userkaf h at left, showFade
            $ chc = 0
            python:
                chc = leader + housee
                if temtem == 0:
                    chc += 2

            menu allchat:
                "Minas":
                    u "{cps=20}Minas.{/cps}"
                    show minas h at right, showFade:
                        zoom 0.8
                    pause 1.0
                    menu minchat:
                        "Ask him why he gave Eya the lead" if (leader == 0):
                            u "{cps=20}Why did you give Eya the lead?{/cps}"
                            m "{cps=20}I thought she'll be better.{/cps}"
                            u "{cps=20}Who knows.{/cps}"
                            $ leader = 1
                            $ chc += 1
                            call minchat
                        "Ask him where Eya lives" if (housee == 0):
                            u "{cps=20}Have you taken lot of time when you went with Eya and Tausert?{/cps}"
                            m "{cps=20}No it wasn't too long.{/cps}"
                            m "{cps=20}We moved straight beside the Nile and arrived.{/cps}"
                            u "{cps=20}Mhm nice.{/cps}"
                            $ housee = 1
                            $ chc += 1
                            call minchat
                        "Tell him about the fight" if (temtem == 1) and (mfd == 0):
                            show userkaf n at left
                            u "{cps=20}I saw a dream this morning.{/cps}"
                            m "{cps=20}What was it about?{/cps}"
                            show minas n at right:
                                zoom 0.8
                            u "{cps=20}We fought.{/cps}"
                            m "{cps=20}Huh ...{/cps}"
                            m "{cps=20}That will never happen.{/cps}"
                            u "{cps=20}I believe.{/cps}"
                            $ mfd = 1
                            $ chc += 1
                            show userkaf h at left
                            show minas h at right:
                                zoom 0.8
                            call minchat
                        "Leave him":
                            show minas h at right, hideFade:
                                zoom 0.8
                            hide minas h
                            pause 1.0
                            call allchat

                "Eya":
                    u "{cps=20}Eya.{/cps}"
                    show eya h at right, showFade
                    pause 1.0
                    menu eyachat:
                        "Tell her about the dream" if (temtem == 1) and (efd == 0):
                            show userkaf n at left
                            show eya c at right
                            u "{cps=20}I had a bad dream.{/cps}"
                            e "{cps=20}What was it about?{/cps}"
                            show userkaf s at left
                            u "{cps=20}You ...{/cps}"
                            e "{cps=20}What?{/cps}"
                            u "{cps=20}We lost.{/cps}"
                            e "{cps=20}We won't ...{/cps}"
                            show eya h at right
                            show userkaf h at left
                            e "{cps=20}It's just a dream.{/cps}"
                            $ efd = 1
                            $ chc += 1
                            jump eyachat

                        "Offer her a drink" if chc == 5:
                            show eya b at right
                            u "{cps=20}Wanna have a drink?{/cps}"
                            show eya h at right
                            e "{cps=20}Sure .. Let's watch the shows together.{/cps}"
                            scene black with dissolve
                            "{cps=20}1 hour later ...{/cps}"
                            
                            


                        "Leave her":
                            show eya h at right, hideFade
                            hide eya h
                            pause 1.0
                            call allchat
                            
                "Tausert":
                    u "{cps=20}Tausert.{/cps}"
                    show tausert h at right, showFade
                    pause 1.0
                    menu tauchat:
                        "Tell her about the dream" if (temtem == 0) and (tfdd == 0):
                            show userkaf n at left
                            u "{cps=20}I had a dream.{/cps}"
                            t "{cps=20}What was it?{/cps}"
                            u "{cps=20}We were divided into 2 teams ...{/cps}"
                            u "{cps=20}And there was a temple ...{/cps}"
                            u "{cps=20}But we didn't explore it.{/cps}"
                            t "{cps=20}Mhm interesting.{/cps}"
                            show userkaf h at left
                            $ tfdd = 1
                            $ chc += 1
                            jump tauchat
                        
                        "Tell her about the dream" if (temtem == 1) and (tfd == 0):
                            show userkaf n at left
                            u "{cps=20}I had a dream.{/cps}"
                            t "{cps=20}What was it?{/cps}"
                            show userkaf s at left
                            show tausert z at right

                            u "{cps=20}Eya died.{/cps}"
                            t "{cps=20}Huh how?{/cps}"
                            u "{cps=20}I don't know.{/cps}"
                            t "{cps=20}Don't tell her.{/cps}"
                            u "{cps=20}No don't worry.{/cps}"
                            show tausert h at right
                            show userkaf h at left
                            $ tfd = 1
                            $ chc += 1
                            jump tauchat

                        "Leave her":
                            show tausert h at right, hideFade
                            hide tausert h
                            pause 1.0
                            call allchat
    
    scene bg square with pixellate
    pause 1.5


    show cheif at center, showFade
    pause 1.0
    pause 1.0
    V "{cps=10}As we thank the Nile for his kindness ...{/cps}"
    V "{cps=10}He should have Guardians ...{/cps}"
    V "{cps=10}And now ... {w=0.5} For the waited one ...{/cps}"
    V "{cps=5}Guardians Of The Nile{/cps}"
    V "{cps=10}I'll anounce the rules of this season.{/cps}"
    V "{cps=10}This year, {w=0.5} it will be held on 5 days.{/cps}"
    V "{cps=10}We'll start with a simple running race today.{/cps}"
    V "{cps=10}Get ready.{/cps}"
    show cheif at center, hideFade with dissolve
    hide cheif
    pause 1.5


    show minas z at p1, showFade:
        zoom 0.8

    show userkaf z at p2, showFade
    show eya z at p3, showFade
    show tausert z at p4, showFade
    pause 1.0

    e "{cps=20}Huh ?!{/cps}"

    menu:
        "Intaf Intaf haha.":
            show userkaf h at p2
            u "{cps=20}Intaf Intaf haha.{/cps}"
            e "{cps=20}No time for that.{/cps}"
            show userkaf z at p2
        
    show tausert h at p4
    t "{cps=20}Don't worry guys ...{/cps}"
    t "{cps=20}It doesn't differ what game we play first.{/cps}"
    m "{cps=20}But he said there will be 5 days not 3.{/cps}"
    u "{cps=20}Maybe they increased games.{/cps}"
    e "{cps=20}Or decreases games per day.{/cps}"
    t "{cps=20}Whatever !{/cps}"
    t "{cps=20}We will still win.{/cps}"
    u "{cps=20}Shhh he'll speak now.{/cps}"
    show minas a at p1:
        zoom 0.8
    m "{cps=10}SILENCE.{/cps}"
    menu:
        "Laugh with them":
            show userkaf h at p2
    show eya h at p3
    show tausert h at p4
    'All' "{cps=20}Hahaha.{/cps}"

    V "{cps=10}SILENCE.{/cps}"
    show minas h at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf h at p2, hideFade with dissolve
    show eya h at p3, hideFade with dissolve
    show tausert h at p4, hideFade with dissolve
    hide minas h
    hide userkaf h
    hide eya h
    hide tausert h
    pause 1.5
    show cheif at center, showFade
    pause 1.0

    V "{cps=10}The rules are simple ...{/cps}"
    V "{cps=10}A player from each team holds a flag and stands on the start line ...{/cps}"
    V "{cps=10}And the other players stand in another checkpoints ...{/cps}"
    V "{cps=10}Each player gives the flag to the next player till the last one ...{/cps}"
    V "{cps=10}And ...{/cps}"
    V "{cps=10}One team will be eliminated ...{/cps}"
    V "{cps=10}Good look kids.{/cps}"
    
    show cheif at center, hideFade
    hide cheif
    pause 1.0

    show minas h at p1, showFade:
        zoom 0.8

    show userkaf h at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade
    pause 1.0

    t "{cps=20}I told you not to worry.{/cps}"
    m "{cps=20}Only one team will be eliminated.{/cps}"
    u "{cps=20}Well, the race is guarnteed, isn't it leader?{/cps}"
    e "{cps=20}Sure Userkaf.{/cps}"
    e "{cps=20}Userkaf ... {w=0.2} Can we talk in private?{/cps}"
    u "{cps=20}Of course.{/cps}"

    show minas h at p1, hideFade:
        zoom 0.8
    hide minas h
    show tausert h at p4, hideFade
    hide tausert h
    pause 1.0

    menu:
        "What do you need Eya?":
            u "{cps=20}What do you need Eya?{/cps}"
            e "{cps=20}I should choose who stands where.{/cps}"
            e "{cps=20}What do you suggest?{/cps}"
            menu:
                "Suggest":
                    u "{cps=20}I suggest ...{/cps}"
                    menu:
                        u "{cps=20}I suggest ...{/cps}"
                        "Start with Minas":
                            u "{cps=20}Start with Minas he's the slowest ...{/cps}"
                            u "{cps=20}And end with you, you're the best {w=0.2} at running.{/cps}"
                            

    e "{cps=20}Thanks Userkaf.{/cps}"
    u "{cps=20}Anytime Eya.{/cps}"
    pause 1.0

    show minas n at p1, showFade:
        zoom 0.8

    show tausert n at p4, showFade
    pause 1.0

    t "{cps=20}So what leader?{/cps}"
    e "{cps=20}We'll start with Minas then you, Userkaf and me at last.{/cps}"
    m "{cps=20}Well.{/cps}"

    V "{cps=10}The starters go with my brother and the rest come with me.{/cps}"
    pause 1.0
    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf h at p2, hideFade with dissolve
    show eya h at p3, hideFade with dissolve
    show tausert n at p4, hideFade with dissolve
    hide minas n
    hide userkaf h
    hide eya h
    hide tausert n
    pause 1.5

    jump d4s4

    return 

label d4s4:
    scene bg street3 with pixellate
    pause 1.0

    show userkaf n at left, showFade
    pause 1.5
    
    show eya h at right, showFade
    show userkaf h at left
    pause 1.0

    u "{cps=20}Oh EYA.{/cps}"
    e "{cps=20}Our checkpoints are so near.{/cps}"
    e "{cps=20}DID YOU KNOW THAT USERKAF !{/cps}"
    u "{cps=20}Haha no.{/cps}"
    menu:
        "I've seen this place before.":
            show userkaf n at left
            u "{cps=20}I've seen this place before.{/cps}"
            e "{cps=20}Of course we're still in Aswan.{/cps}"
            u "{cps=20}No I mean .. I dreamt of it.{/cps}"
    
    e "{cps=20}Oh they're starting, let's talk later.{/cps}"
    u "{cps=20}Good luck.{/cps}"

    show eya h at right, hideFade
    hide eya h
    pause 1.5

    u "{cps=20}Oh my God Minas is so slow.{/cps}"
    pause 2.0
    u "{cps=20}I got bored.{/cps}"
    menu:
        "Stay in your position":
            pause 3.0
            u "{cps=20}That was a clear throw.{/cps}"
            u "{cps=20}Tausert has the first position now.{/cps}"


    menu:
        "Go check the temple":
            show userkaf h at left, hideFade
            hide userkaf h
            e "{cps=40}USERKAF!{/cps}"
            show eya a at right, showFade
            pause 1.0
            show eya a at right, hideFade
            hide eya a

            e "{cps=40}Come with me!{/cps}"
            menu:
                "Go with her":
                    u "{cps=20}Okay.{/cps}"
            show userkaf n at left, showFade
            show eya a at right, showFade
            e "{cps=40}What were you thinking of?{/cps}"
            e "{cps=40}Run fast.{/cps}"
            pause 1.0
            show userkaf n at right, hideFade
            hide userkaf n

            jump d4s5
            
    return

label d4s5:
    scene bg street2 with pixellate
    show minas z at p1, showFade:
        zoom 0.8
    show userkaf z at p2, showFade
    show tausert z at p4, showFade
    pause 1.0
    t "{cps=20}Oh my God she's so late.{/cps}"
    m "{cps=20}It's because of you Userkaf ... It's because of you.{/cps}"
    show userkaf s at p2
    pause 3.0

    show eya a at p3, showFade
    show minas a at p1:
        zoom 0.8
    show tausert a at p4
    
    e "{cps=20}We could have lost because of you Userkaf.{/cps}"
    menu:
        "Apologize":
            u "{cps=20}I'm sorry guys.{/cps}"

    
    show eya n at p3
    show minas n at p1:
        zoom 0.8
    show tausert n at p4
    show userkaf h at p2
    e "{cps=20}No worries Userkaf.{/cps}"
    pause 2.0

    show userkaf n at p2
    V "{cps=10}One team is eliminated ...{/cps}"
    V "{cps=10}10 teams are remaining ...{/cps}"
    V "{cps=10}See you tommorow.{/cps}"
    pause 2.5

    t "{cps=20}Let's go to the palm tree.{/cps}"
    menu:
        "Let's go":
            u "{cps=20}Let's go.{/cps}"

    pause 1.0
    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    show userkaf n at p2, hideFade with dissolve
    show eya n at p3, hideFade with dissolve
    show tausert n at p4, hideFade with dissolve
    hide minas n
    hide userkaf n
    hide eya n
    hide tausert n
    pause 1.5
    
    jump d4p2

    return

label d4p2:
    scene bg palm1 with pixellate
    pause 1.0

    show minas h at p1, showFade:
        zoom 0.8

    show userkaf h at p2, showFade
    show eya h at p3, showFade
    show tausert h at p4, showFade
    pause 1.0

    u "{cps=20}It was a great day for real.{/cps}"
    e "{cps=20}Yeah.{/cps}"
    t "{cps=20}That jump was facsinating Minas.{/cps}"
    u "{cps=20}Indeed.{/cps}"
    m "{cps=20}Thanks.{/cps}"
    u "{cps=20}Aha that's why the Cheif said ...{/cps}"
    e "{cps=20}Be ready ...{/cps}"
    t "{cps=20}No one knows tomorrow ...{/cps}"
    m "{cps=20}Should the moral be that easy?{/cps}"
    e "{cps=20}Should it be hard?{/cps}"
    u "{cps=20}Maybe there's more than one?{/cps}"
    t "{cps=20}Or maybe that's not even the moral{/cps}"
    u "{cps=20}Whatever .. We'll know later.{/cps}"
    e "{cps=20}So we have nothing to do.{/cps}"
    u "{cps=20}Yes for the contest ...{/cps}"
    u "{cps=20}We can do other things.{/cps}"
    t "{cps=20}I got tired from that race.{/cps}"
    show userkaf n at p2
    u "{cps=20}Bruh.{/cps}"
    e "{cps=20}Me too, I want to go home.{/cps}"
    m "{cps=20}Same for me.{/cps}"
    u "{cps=20}Okay later then.{/cps}"

    pause 1.0
    show minas n at p1, hideFade with dissolve:
        zoom 0.8
    show eya n at p3, hideFade with dissolve
    show tausert n at p4, hideFade with dissolve
    hide minas n
    hide eya n
    hide tausert n
    pause 1.5
    

    menu:
        "Go for a walk":
            show userkaf n at p2, hideFade with dissolve
            hide userkaf n
            jump d4s6


    return

label d4s6:
    scene bg street1 e with pixellate
    pause 1.0

    show userkaf n at left, showFade
    pause 1.0
    show stranger at right, showFade
    pause 1.5

    show userkaf h at left
    u "{cps=20}Hello hello.{/cps}"
    ss "{cps=20}Hi kid.{/cps}"
    show userkaf n at left
    u "{cps=20}I was searching for you.{/cps}"
    ss "{cps=20}Oh really why?{/cps}"
    u "{cps=20}I had a lot inside me.{/cps}"
    ss "{cps=20}Speak kid.{/cps}"

    menu:
        "Think of another idea":
            u "{cps=20}I'm good now.{/cps}"
            ss "{cps=20}Okay.{/cps}"
            

    u "{cps=20}Anyways I'll check on you later.{/cps}"
    u "{cps=20}Wait ...{/cps}"
    u "{cps=20}What's your name?{/cps}"
    ss "{cps=20}Haha .. Just call me anything.{/cps}"
    u "{cps=20}Okay .. Mr. Anything !{/cps}"
    ss "{cps=20}Whatever.{/cps}"
    pause 1.0
    show stranger at right, hideFade
    hide stranger
    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade
            hide userkaf n
            pause 1.0
            jump d4r4

    return

label d4r4:
    scene bg ubd2 with pixellate
    pause 1.0

    show userkaf h at left, showFade
    pause 1.0

    menu:
        "Write a short a message":
            "{cps=15}You {w=0.1}make me {w=0.3}think long!"

    menu:
        "Take it to her":
            show userkaf n at left, hideFade
            hide userkaf n
            pause 1.0
            jump d4s7
    return

label d4s7:
    scene bg street1 n with pixellate
    pause 1.0
    show userkaf n at left, showFade
    pause 1.0

    u "{cps=20}Bruh .. It's gotten late"

    menu:
        "Continue":
            u "{cps=20}Nothing would happen."
            show userkaf n at left, hideFade
            hide userkaf n
            pause 1.0
            jump d4s8


    return

label d4s8:
    scene house eya n with pixellate
    pause 1.0
    show userkaf n at right, showFade
    pause 1.0

    menu:
        "Throw the message in the yard":
            u "{cps=20}Well done."
            show userkaf n at left, hideFade
            hide userkaf n
            pause 1.0
            jump d4s9

    return

label d4s9:
    scene bg street1 n with pixellate
    pause 1.0
    show userkaf h at left, showFade
    pause 1.0

    show stranger at right, showFade
    pause 1.0

    ss "{cps=20}Night has fallen, why aren't you home?"

    menu:
        "I was taking a walk":
            u "{cps=20}I was taking a walk."

    ss "{cps=20}You should go home."
    u "{cps=20}Of course."
    u "{cps=20}See you."

    show userkaf n at left, hideFade
    hide userkaf n
    pause 1.0
    jump d4r5


    return
    
label d4r5:
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

            u "{cps=20}That was a long day.{/cps}"


            show mirror3 at hideFade with dissolve
            hide mirror3
            jump d4r5


        "Go to the kitchen":
            u "{cps=20}Let's eat something.{/cps}"
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            jump d4k5

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            
            show expression papyrusN with dissolve

            u "{cps=20}I have 1 .. you have 2.{/cps}"


            show expression papyrusN at hideFade with dissolve
            hide expression papyrusN
            jump d4r5

        "Sleep":
            scene black with dissolve
            pause 1.0
            u "{cps=20}Will she read it?{/cps}"
            pause 2.0
            u "{cps=20}I haven't seen father since the draw day.{/cps}"
            u "{cps=20}Maybe he's in a hunting trip.{/cps}"
            jump day5

    return

label d4k5:
    scene bg kitchen3
    with pixellate
    pause 1.5
    show userkaf n at left, showFade
    pause 1.0
    
    menu:
        "Eat an apple":
            u "{cps=20}Tasty.{/cps}"
            jump d4k5

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d4r5

    return    
