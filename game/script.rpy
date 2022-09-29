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
    "Prologue Intro":
        hide ScSeTx with dissolve
        jump prologue_intro
    "Prologue Concert End":
        hide ScSeTx with dissolve
        jump prologue_concert_end
    "Experimental Section":
        hide ScSeTx with dissolve
        jump experimental
    "End":
        hide ScSeTx with dissolve
        jump end_of_wip
label scene_bookends: ## Copy when making new scene
    "{i}scene_bookend start{/i}"
    "{i}scene_bookend end{/i}"
    scene b-blackscreen with dissolve
    pause 1
label prologue_intro:
    "{i}Prologue, Scene 1*{/i}"
    "{i}Before the Concert{/i}"
    #[mc is seated on a bench in the city’s largest park, gazing into the darkening sky]
    "(Some kind of profound monologue regarding his current view of the world, idfk)"
    mc  "(I was so lost in thought that I hadn’t noticed how long I had been sitting here, waiting.)"
    #[A can of chilled soda appears as the text is read]
    mc  "(It was only when I had felt the touch of an ice cold object pressed against the nape of my neck that I realized I had been daydreaming)"
    #[Silhouette of Brandon’s sprite appears, as screen shakes to signify mc jolting up]
    mc  "?!"
    "???"  "Oh, hey, you are awake."
    #[Pulling out his phone to see the time was now 6:34 PM]
    mc  "Yeah, I am. You’re cutting it close. What took you so long?" #[Slightly annoyed tone]
    #[Brandon’s silhouette fully becomes the character’s sprite]
    bra "Missed the damn train because I had to make a stop. Got us some drinks and snacks, see?" #[Lifts up a convenience store bag full of items]
    mc  "(The person that had just risen me from my stupor was my close friend, Brandon Marsh. We’ve known each other since we were kids, but we didn’t really grow up together. I only ever saw him when I would visit my grandparents here in the city, since his house was just down the road.)"
    mc  "(You could probably tell from his mannerisms and appearance, but he’s not from Japan. He tells me that when he was 2 years old, his parents were so fascinated by the country that they moved here, though that wasn’t without some issues.)"
    mc  "(Because of this, he was raised by both the Japanese school system and the American mannerisms that his parents carried over from their last residence. The first time I met him, I was 5 years old, and we've become good friends since.)"
    #[Standing up from the bench]
    mc  "I guess that saves us some money, then. C’mon, the show starts at 7, and we still have to get through the line at security"
    bra "Shit, you’re right. Yeah, let’s hurry"
    #[mc and Brandon begin walking further through the park to the concert venue, which is a stage set up near the center of the grass]
    bra "So what made you a fan of this Scarlett girl? I didn’t think you were the type to follow anything idol related."
    mc  "Well, sometime before I moved here, I was scrolling through a bunch of channels. One of them was this broadcast showcasing a bunch of up-and-coming artists. Most of them didn’t really stand out to me. Felt like they were all part of this blur"
    #[Looking to the side at mc]
    bra "But she did, huh?"
    mc  "Yeah… I don’t know what it was about her."
    #[mc begins to look up to the sky, in which the sun had already set]
    mc  "She just felt so vibrant, you know? Singing those songs all while dancing with a smile. It all just felt… cool, I guess. I don’t know, she just feels right to me, like she just knew how to pique my fancy"
    #[Camera cuts back to scene]
    bra "And that’s why you wanted to go to the first concert available, to see your new favorite idol live?"
    mc  "Yeah, you caught me" #[Mockingly defeated tone]
    bra "I thought that was the case. Because I thought you’d wanna see more of Scarlett tonight…"
    #[Brandon pulls out 2 tickets from his hoodie pockets, and hands one to mc]
    bra "...I got us these"
    mc  "No way, are those the deluxe tickets that sold out weeks ago?"
    bra "Sure are"
    mc  "Don’t these cost quite a bit? I’ll pay you back later, when I can"
    #[Waving his hand in front of him dismissively]
    bra "Nah, don’t sweat it. Just think of this as a welcome gift from me."
    mc  "Oh, well, thanks dude. This is actually a really nice thing of you to do for once"
    bra "Like I’m ever not nice" #[Sarcastically]
    mc  "Well, it’s a good thing you told me now, because there’s a second line for special ticket holders to go right through"
    #[mc points at a shorter, much faster line into the venue with a sign that reads "deluxe patrons only"]
    bra "I knew I made the right call to make that stop"
    mc  "What was that?" #[Quizzically]
    bra "Nothing, let’s head in"
    mc  "(The wait had just barely reached the 5 minute mark when we got cleared to enter. It was now 6:50, ten minutes until showtime. And the other line looked like it wouldn’t be fully cleared until after the show had already started. I silently thanked Brandon again for getting these tickets as we headed in)"
    #[Scene transitions to the concert]
    mc  "(The crowd was unlike anything I had seen before. At least a thousand or two strangers crammed into this small section of the park. There was no ceiling, so you could look up and see the night sky. The stage spotlights were currently aimed at the crowd as one of the sole sources of light for the crowd to see and navigate with. But thanks to our nearly late arrival, Brandon and I were stuck near the rear middle, a good 15 rows away from the stage. But I could thankfully still see the stage clearly, the sea of heads indicative of just how popular Scarlett must be. Before long, the voice of a hypeman roars through the speakers.)"
    "Hypeman" "Alright, you precious little Roses. You’ve been waiting long enough. Give some cheer to your darling senpai, Scarlett!"
    #[The crowd begins counting down with the hypeman]
    "Hypeman" "In 5… 4…. 3… 2… 1…"
    mc  "(When the countdown had reached zero, all the lights in the area had shut off. In this period of pitch black respite, a wave of glow sticks from raving fans had emerged, dimly illuminating the restless and excited crowd. When the stage lighting had reactivated, there stood Scarlett, who opened up her performance with her iconic line)"
    sca "Heeeeyyyy, everyone~"
    #[Sounds of the roaring crowd following this opening line]
    sca "How are my lovely little Roses doing on this fine evening? I hope you’re prepared to get pumped up, because the show starts now!"
    mc  "(The instrumental of her latest single began to play, as the crowd cheered Scarlett on. The vibrant flashing lights, in conjunction with Scarlett’s stellar singing and captivating rhythmic dances, had created a vivid image that could never be achieved by just viewing a televised broadcast. This was here. This was now. This was Scarlett’s magic spell in action. I stood there in awe, unable to even cheer myself with just how incredible this spectacle was. At least an hour had gone by with this routine keeping my attention in this tunnel visioned daydream. Before I realized, the performance had come to an end and I was left wanting for more. The sounds of encore raging throughout the park awoke me, along with an announcement from Scarlett herself)"
    sca "This isn’t the end yet, Roses. You dedicated fans already know that just after this, there will be a meet and greet Q&A panel, where you can request any question of your darling senpai, at the adjacent tent. See you there, lovelies."
    #[Scarlett then walks towards the backstage, vanishing behind the curtains]
    mc  "(Seemingly reading my mind, I felt Brandon tap my shoulder, speaking to me.)"
    bra "That’s us, get your ticket ready"
    mc  "Yeah, I have it here. We should head over"
    #[mc and Brandon begin to walk over to the exit and towards the neighboring tent]
    "{i}Scene End{/i}"
    scene b-blackscreen with dissolve
    pause 1
label prologue_concert_end:
    "{i}Prologue, Scene 2*{/i}"
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
    mc  "Says the one who made us snacks, don’t act like you’re not into it."
    #bradon smiling
    show a-bra smile
    bra "Into baking sweets and watching you fangirl? Absolutely."
    bra "But I will say, Scarlett is pretty sweet."
    mc  "Isn’t she? I knew you’d get it."
    #brandon slight frown
    show a-bra frown
    bra "Oh cool, you’re doing that selective hearing thing again.."
    show a-mc:
        linear 0.2 ftr
        pause 0.2
        linear 0.5 xr
    mc  "LET’S GO MEET SCARLETT!"
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
    mc  "…"
    mc  "(DAMMIT! NOW THAT I’M HERE, WHAT DO I SAY!)"
    mc  "(OH MY GOD, SHE'S ACTUALLY IN FRONT OF ME!)"
    show a-bra frown
    "Not Brandon" "(You can take five guys, but not this?)"
    mc  "(How the hell does he always do that?)"
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
    mc  "Right! I-I’m a huge fan, I just wanted to say I’ve been a fan for a long time and your music has helped me a lot!"
    mc  "I was hoping you could sign this."
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
    mc  "You’re really asking to get put on your ass."
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
    mc  "I’ll be there!"
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
    mc  "(I love this town.)"
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
