label day5:
    scene black with dissolve
    pause 5.0

    jump d5s1

    return

label d5s1:
    scene bg street3 with pixellate
    pause 1.0
    
    show userkaf n at right, showFade
    pause 1.0
    u "{cps=20}Mhm.{/cps}"

    menu:
        "Explore the temple":
            show userkaf n at right, hideFade
            hide userkaf n
            scene bg temple1 with pixellate
            pause 1.0
            show userkaf n at right, showFade
            pause 3.0
            show userkaf z at right
            pause 0.5
            scene bg street3
            "{cps=20}AHHHHHHHHHHHHHH.{/cps}"
            scene black
            "{cps=20}What was that scream?{/cps}"
            "{cps=20}Is Userkaf's father really missing?{/cps}"
            "{cps=20}And the most important ...{/cps}"
            "{cps=20}Will Eya know who is sender of the letter?{/cps}"
            "{cps=20}Wait for next update :){/cps}"
            "{cps=20}Don't forget to play with another scenarios!{/cps}"
            "{cps=20}Thank You.{/cps}"


    return