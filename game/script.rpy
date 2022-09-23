##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################

### Screen Locations
##   x only   ## These only effect left/right position, not up/down
transform lx:#Just off screen left
    xanchor 1.0 xpos 0.0
transform lw:#Just on screen against left wall
    xalign 0.0
transform l7:
    xcenter -0.2
transform l6:
    xcenter -0.1
transform l5:##Split across left wall
    xcenter 0.0
transform l4:
    xcenter 0.1
transform l3:
    xcenter 0.2
transform l2:
    xcenter 0.3
transform l1:
    xcenter 0.4
transform c0:#Centered
    xcenter 0.5
transform r1:
    xcenter 0.6
transform r2:
    xcenter 0.7
transform r3:
    xcenter 0.8
transform r4:
    xcenter 0.9
transform r5:#Split across right wall
    xcenter 1.0
transform r6:
    xcenter 1.1
transform r7:
    xcenter 1.2
transform rw:#Just on screen against right wall
    xalign 1.0
transform rx:#Just off screen right
    xcenter 1.0
transform xl:#Exit Left
    xcenter -2.0
transform xr:#Exit Right
    xcenter 3.0
    ##   Other   ##
transform ax:#centered 1 screen height above - For tripple height BGs
    ypos -.5 yanchor 0.5
    #ypos 0.0
transform cx:#Aligned against ceiling
    ypos 0.0 yalign 0.0
transform fx:#Aligned against floor
    ypos 1.0 yalign 1.0
transform bx:#centered 1 screen height below - For tripple height BGs
    ypos 1.5 yanchor 0.5
    #ypos 1.0
transform cc:# Cerner screen - For Mini-CG / Chibi
    ycenter 0.5
    xcenter 0.5
transform ftr:# Faces sprites toward the right
    xzoom -1.0
    ##   Animation   ##
transform bounce:# makes the sprite jump
    linear 0.1 yoffset -40
    pause 0.1
    linear 0.1 yoffset 0
transform nod:# makes the sprite bow/nod
    linear 0.2 yoffset 40
    pause 0.4
    linear 0.2 yoffset 0
transform shake:# makes the sprite shake left/right
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40
    linear 0.1 xoffset 40
    linear 0.1 xoffset -40


### Character Shorthands
#main
define mc = Character("MC",color="#267f00")
define gei = Character("Geisha",color="#000000")
define har = Character("Haruka",color="#000000")
define krr = Character("Kirara",color="#000000")
define sca = Character("Scarlet",color="#900000")
define sco = Character("Scotlyn",color="#000000")
#Side
define bra = Character("Brandon",color="#0094ff")
define bri = Character("Brianne",color="#000000")
define fum = Character("Fumika",color="#000000")
define kao = Character("Kaori",color="#000000")
define nek = Character("Nekome",color="#000000")
define sho = Character("Shoko",color="#000000")
define rin = Character("Rin",color="#000000")
define tog = Character("Toge",color="#000000")
define nad = Character("Nadeshiko",color="#000000")
#NRC
define ats = Character("Atsuko",color="#000000")
define kan = Character("Kanou",color="#000000")
define sjk = Character("Scott JK",color="#000000")
define sor = Character("Sora",color="#000000")
define tam = Character("Tamashii",color="#000000")
define yur = Character("Yuri",color="#000000")
#WW
define alf = Character("Alfred",color="#000000")
define asm = Character("Asmund",color="#000000")
define dad = Character("Dad",color="#000000")
define may = Character("Mayor",color="#000000")
define sam = Character("Sams",color="#000000")
#???
define mar = Character("Mari",color="#000000")
define oto = Character("Otto",color="#000000")

## Misc

#
#image shortname = Movie(play="filename.ogv", pos=(0, 0), anchor=(0, 0))
#    e "For example, we might want to have text that is {b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, or {u}underlined{/u}."




label start: ### Start Of Game
    "Welcome to the WIP Weaving hearts VN"
    ### Dev Scene Select
    image ScSeTx = Text(_("Dev Scene select"), size=120)
    show ScSeTx with dissolve:
        c0
        ypos 0.1
menu:
    "Prologue":
        hide ScSeTx with dissolve
        jump prologue_scene_1
    "Experimental Section":
        hide ScSeTx with dissolve
        jump experimental
    "End":
        hide ScSeTx with dissolve
        jump end_of_wip
label prologue_scene_1:
    "{i}Prologue, Scene 1{/i}"
    ##concert scene at night.
    scene b-stage n1
    "{i}b-stage n1.png - Stage BG night{/i}"
    #scarlett excited
    show cm-concertzoom 1 at cc with dissolve
    "{i}cm-concertzoom 1.png - Agreed mini-CG showing a closeup of scarlet on stage{/i}"
    sca "I hope everyone has had as much fun as I have!"
    "Crowd" "YEAH!!!!"
    show cm-concertzoom 2
    sca "The meet and greet starts in half an hour, so make sure to stick around!"
    show cm-concertzoom 1
    sca "It's going to be awhile before my next concert, so I'd like to make this count! See you all in a few!"
    hide cm-concertzoom with dissolve
    ##crowd in background, at crowd level
    ##brandon appears mid-screen
    #brandon smug
    show a-bra smug:
        ftr
        l3
        bx
        ease 1.0 fx
    show a-mc smile:
        r3
        bx
        ease 1.0 fx
    bra "Wow, what a first date, didn’t think it’d be so glamorous."
    bra "I kinda had a feeling you were excited to see me again, but damn, didn’t think you’d go this far."
    mc "Says the one who made us snacks, don’t act like you’re not into it."
    #bradon smiling
    show a-bra smile
    bra "Into baking sweets and watching you fangirl? Absolutely."
    bra "But I will say, Scarlett is pretty sweet."
    mc "Isn’t she? I knew you’d get it."
    #brandon slight frown
    show a-bra frown
    bra "Oh cool, you’re doing that selective hearing thing again.."
    show a-mc:
        linear 0.2 ftr
        pause 0.2
        linear 0.5 xr
    mc "LET’S GO MEET SCARLETT!"
    ##mc fades from screen
    bra "{cps=*0.1}Aaaand{/cps} he’s gone."
    show a-bra:
        linear 4.0 xr
    show b-blackscreen with dissolve
    ##same crowd scene just after transition
    ##scarlett enters mid-screen
    #scarlett happy
    show a-bra neutral at l4
    show a-mc awkward at l2
    show a-sca smile at r3
    show a-mc:
        ease 1.0 l1
    hide b-blackscreen with dissolve
    pause 0.5
    sca "Hi, it’s nice to meet you! As you know, I’m Scarlett! Always awesome to see a new fan!"
    mc "…"
    mc "(DAMMIT! NOW THAT I’M HERE, WHAT DO I SAY!)"
    mc "(OH MY GOD, SHE'S ACTUALLY IN FRONT OF ME!)"
    show a-bra frown
    "Not Brandon" "(You can take five guys, but not this?)"
    mc "(How the hell does he always do that?)"
    #scarlett nervous smile
    show a-sca awkward
    sca "{cps=*0.1}Soooo,{/cps} {w=1.0} {cps=*0.5}what’s your name?{/cps}"
    python:
        mcn = renpy.input(_("What {i}is{/i} my name?"))
        mcn = mcn.strip() or "MC"
    #brandon enters left side
    show a-bra smile:
        ease 1.0 l3
    bra "Hey, I’m Brandon and this is [mcn], sorry he’s weird."
    bra "Great show by the way."
    #scarlett excited
    show a-sca laugh:
        bounce
    sca "Thank you! I’m glad you liked it! I always try to put on a good show!"
    #brandon angry
    show a-bra angy
    "..."
    #brandon shakes MC
    #scarlett shocked
    show a-bra:
        linear 0.2 l2
        shake
    pause 0.2
    show a-mc gya:
        shake
    show a-sca scared:
        linear 0.2 r4
    pause 1.0
    bra "You were so excited, say something, idiot!"
    show a-sca awkward
    show a-mc awkward:
        ease 0.5 c0
    mc "Right! I-I’m a huge fan, I just wanted to say I’ve been a fan for a long time and your music has helped me a lot!"
    mc "I was hoping you could sign this."
    #scarlet hops twice
    show a-sca laugh:
        bounce
        bounce
    #scarlet happy
    pause 1.0
    show a-sca laugh
    sca "Absolutely!"
    #brandon smug
    show a-bra smug
    show a-mc smile:
        ease 1.0 r1
    show a-sca:
        ease 0.5 r3
        pause 0.5
        ease 0.3 yoffset 20
    bra "Hey, you did it! My boys all grown up!"
    mc "You’re really asking to get put on your ass."
    bra "If you're offering."
    #brandon smile
    show a-bra smile
    show a-sca:
        ease 0.3 fx
        pause 0.3
        ease 0.3 yoffset 0
    sca "Here you go! Hope to see you at my next concert!"
    show a-mc:
        ease 0.5 c0
    mc "I’ll be there!"
    show a-sca:
        nod
    show a-mc:
        nod
    #sacrlett fades from screen
    #brandon fades from screen
    pause 0.8
    show a-sca:
        linear 0.5 alpha 0.0
    show a-bra:
        linear 0.5 alpha 0.0
    mc "(I love this town.)"
    scene b-blackscreen with dissolve
    pause 1
    "{i}This is the end of the WIP script{/i}"
    #this is a test line from Able98Able98
    #This is another test line from able98able98
label experimental:
    "{i}Start of Experimental section{/i}"
    "This game has a patent pending Sakura mode for H scenes to make them SFYT and ease editing"
    show d-sakura petal with dissolve:
        alpha 0.5
        yoffset -30
menu:
    "Do you want to enable Sakura mode?"
    "Yes":
        jump sakura_ena
    "No":
        jump sakura_dis
label sakura_ena:
    $ sakura_flag = True
    show d-sakura:
        linear 0.5 alpha 1.0
    "Sakura mode enabled"
    jump sakura_conf
label sakura_dis:
    $ sakura_flag = False
    show d-sakura:
        linear 0.5 alpha 0.0
    "Sakura mode disabled"
    jump sakura_conf
label sakura_conf:
    scene b-blackscreen with dissolve
    "{i}Allong comes an H scene{/i}"
    show a-sca laugh at c0 with dissolve
    image nips = Solid("#900000", xysize=(400, 200))
    image naps = Text(_("Nip Naps"), size=80)
    show nips:
        c0
        ypos 0.65
        alpha 0.0
    show naps:
        c0
        ypos 0.65
        alpha 0.0
    if sakura_flag:
        "Sakura enabled"
        show d-sakura wall:
            c0
            yoffset 600
            zoom 2.1
        show nips:
            alpha 1.0
        show naps:
            alpha 1.0
        show a-sca scared with dissolve
        pause 0.5
        show a-sca awkward with dissolve
    else:
        "Sakura not enabled"
        show nips:
            alpha 1.0
        show naps:
            alpha 1.0
        show a-sca scared with dissolve
    "{i}End of Experimental section{/i}"
    scene b-blackscreen with dissolve
label end_of_wip:
    "{i}This is the end of the WIP game{/i}"
    "{i}The VN will now return to the main menu{/i}"
    scene b-blackscreen with dissolve
    return
##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################
