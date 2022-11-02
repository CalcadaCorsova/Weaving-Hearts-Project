##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################

################################################################################
## Initialization
################################################################################
init offset = -1

################################################################################
## Styles
################################################################################
init -1: ## Styles
    style default:
        properties gui.text_properties()
        language gui.language

    style input:
        properties gui.text_properties("input", accent=True)
        adjust_spacing False

    style hyperlink_text:
        properties gui.text_properties("hyperlink", accent=True)
        hover_underline True

    style gui_text:
        properties gui.text_properties("interface")


    style button:
        properties gui.button_properties("button")

    style button_text is gui_text:
        properties gui.text_properties("button")
        yalign 0.5


    style label_text is gui_text:
        properties gui.text_properties("label", accent=True)

    style prompt_text is gui_text:
        properties gui.text_properties("prompt")


    style bar:
        ysize gui.bar_size
        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

    style vbar:
        xsize gui.bar_size
        top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

    style vscrollbar:
        xsize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style slider:
        ysize gui.slider_size
        base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/slider/horizontal_[prefix_]thumb.png"

    style vslider:
        xsize gui.slider_size
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        thumb "gui/slider/vertical_[prefix_]thumb.png"


    style frame:
        padding gui.frame_borders.padding
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################
init -1: ## Say Screen (Textbox)
    ## Say screen ##################################################################
    ##
    ## The say screen is used to display dialogue to the player. It takes two
    ## parameters, who and what, which are the name of the speaking character and
    ## the text to be displayed, respectively. (The who parameter can be None if no
    ## name is given.)
    ##
    ## This screen must create a text displayable with id "what", as Ren'Py uses
    ## this to manage text display. It can also create displayables with id "who"
    ## and id "window" to apply style properties.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#say

    screen say(who, what):
        style_prefix "say"

        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"


        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0


    ## Make the namebox available for styling through the Character object.
    init python:
        config.character_id_prefixes.append('namebox')

    style window is default
    style say_label is default
    style say_dialogue is default
    style say_thought is say_dialogue

    style namebox is default
    style namebox_label is say_label


    style window:
        xalign 0.5
        xfill True
        yalign gui.textbox_yalign
        ysize gui.textbox_height

        #background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
        background ConditionSwitch(
            "txtbox == 11", Image("gui/textbox11.png", xalign=0.5, yalign=1.0),
            "txtbox == 12", Image("gui/textbox12.png", xalign=0.5, yalign=1.0),
            "txtbox == 13", Image("gui/textbox13.png", xalign=0.5, yalign=1.0),
            "txtbox == 21", Image("gui/textbox21.png", xalign=0.5, yalign=1.0),
            "txtbox == 22", Image("gui/textbox22.png", xalign=0.5, yalign=1.0),
            "txtbox == 23", Image("gui/textbox23.png", xalign=0.5, yalign=1.0),
            "txtbox == 30", Image("gui/textbox30.png", xalign=0.5, yalign=1.0),
            "txtbox == 64", Image("images/d-sakura-p 0.png", xalign=0.5, yalign=1.0),
            "True",         Image("gui/textbox.png",   xalign=0.5, yalign=1.0)
            )

    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ypos gui.name_ypos
        ysize gui.namebox_height

        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        padding gui.namebox_borders.padding

    style say_label:
        properties gui.text_properties("name", accent=True)
        xalign gui.name_xalign
        yalign 0.5

    style say_dialogue:
        properties gui.text_properties("dialogue")

        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
init -1: ## Input Screen
    ## Input screen ################################################################
    ##
    ## This screen is used to display renpy.input. The prompt parameter is used to
    ## pass a text prompt in.
    ##
    ## This screen must create an input displayable with id "input" to accept the
    ## various input parameters.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#input

    screen input(prompt):
        style_prefix "input"

        window:

            vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

                text prompt style "input_prompt"
                input id "input"

    style input_prompt is default

    style input_prompt:
        xalign gui.dialogue_text_xalign
        properties gui.text_properties("input_prompt")

    style input:
        xalign gui.dialogue_text_xalign
        xmaximum gui.dialogue_width
init -1: ## Choice Screen
    ## Choice screen ###############################################################
    ##
    ## This screen is used to display the in-game choices presented by the menu
    ## statement. The one parameter, items, is a list of objects, each with caption
    ## and action fields.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#choice

    screen choice(items):
        style_prefix "choice"

        vbox:
            for i in items:
                textbutton i.caption action i.action


    ## When this is true, menu captions will be spoken by the narrator. When false,
    ## menu captions will be displayed as empty buttons.
    define config.narrator_menu = True


    style choice_vbox is vbox
    style choice_button is button
    style choice_button_text is button_text

    style choice_vbox:
        xalign 0.5
        ypos 405
        yanchor 0.5

        spacing gui.choice_spacing

    style choice_button is default:
        properties gui.button_properties("choice_button")

    style choice_button_text is default:
        properties gui.button_text_properties("choice_button")
init -1: ## Quick Menu Screen (Under Txtbox)
    ## Quick Menu screen ###########################################################
    ##
    ## The quick menu is displayed in-game to provide easy access to the out-of-game
    ## menus.

    screen quick_menu():

        ## Ensure this appears on top of other screens.
        zorder 100

        if quick_menu:

            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 1.0

                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu('preferences')


    ## This code ensures that the quick_menu screen is displayed in-game, whenever
    ## the player has not explicitly hidden the interface.
    init python:
        config.overlay_screens.append("quick_menu")

    default quick_menu = True

    style quick_button is default
    style quick_button_text is button_text

    style quick_button:
        properties gui.button_properties("quick_button")

    style quick_button_text:
        properties gui.button_text_properties("quick_button")

################################################################################
## Main and Game Menu Screens
################################################################################
init -1: ## Navigation (Menu side)
    ## Navigation screen ###########################################################
    ##
    ## This screen is included in the main and game menus, and provides navigation
    ## to other menus, and to start the game.

    screen navigation():
        #zorder 1
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start") action Start()

            else:

                textbutton _("History") action ShowMenu("history")

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Preferences") action ShowMenu("preferences")
            #                                                               ########
            textbutton _("Flowchart") action ShowMenu("flowchart")
            #                                                               ########
            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc"):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action ShowMenu("help")

                ## The quit button is banned on iOS and unnecessary on Android.
                textbutton _("Quit") action Quit(confirm=not main_menu)


    style navigation_button is gui_button
    style navigation_button_text is gui_button_text

    style navigation_button:
        size_group "navigation"
        properties gui.button_properties("navigation_button")

    style navigation_button_text:
        properties gui.button_text_properties("navigation_button")
init -1: ## Main Menu [style]
    style main_menu_frame is empty
    style main_menu_vbox is vbox
    style main_menu_text is gui_text
    style main_menu_title is main_menu_text
    style main_menu_version is main_menu_text

    style main_menu_frame:
        xsize 420
        yfill True

        background "gui/overlay/main_menu.png"

    style main_menu_vbox:
        xalign 1.0
        xoffset -30
        xmaximum 1200
        yalign 1.0
        yoffset -30

    style main_menu_text:
        properties gui.text_properties("main_menu", accent=True)

    style main_menu_title:
        properties gui.text_properties("title")

    style main_menu_version:
        properties gui.text_properties("version")
screen main_menu(): ## Main Menu

    ## Main Menu screen ############################################################
    ##
    ## Used to display the main menu when Ren'Py starts.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#main-menu

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
init -1: ## Game Menu (Right Click Menu)
    ## Game Menu screen ############################################################
    ##
    ## This lays out the basic common structure of a game menu screen. It's called
    ## with the screen title, and displays the background, title, and navigation.
    ##
    ## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
    ## this screen is intended to be used with one or more children, which are
    ## transcluded (placed) inside it.

    screen game_menu(title, scroll=None, yinitial=0.0):

        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

        textbutton _("Return"):
            style "return_button"

            action Return()

        label title

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")


    style game_menu_outer_frame is empty
    style game_menu_navigation_frame is empty
    style game_menu_content_frame is empty
    style game_menu_viewport is gui_viewport
    style game_menu_side is gui_side
    style game_menu_scrollbar is gui_vscrollbar

    style game_menu_label is gui_label
    style game_menu_label_text is gui_label_text

    style return_button is navigation_button
    style return_button_text is navigation_button_text

    style game_menu_outer_frame:
        bottom_padding 45
        top_padding 180

        background "gui/overlay/game_menu.png"

    style game_menu_navigation_frame:
        xsize 420
        yfill True

    style game_menu_content_frame:
        left_margin 60
        right_margin 30
        top_margin 15

    style game_menu_viewport:
        xsize 1380

    style game_menu_vscrollbar:
        unscrollable gui.unscrollable

    style game_menu_side:
        spacing 15

    style game_menu_label:
        xpos 75
        ysize 180

    style game_menu_label_text:
        size gui.title_text_size
        color gui.accent_color
        yalign 0.5

    style return_button:
        xpos gui.navigation_xpos
        yalign 1.0
        yoffset -45
init -1: ## About Screen
    ## About screen ################################################################
    ##
    ## This screen gives credit and copyright information about the game and Ren'Py.
    ##
    ## There's nothing special about this screen, and hence it also serves as an
    ## example of how to make a custom screen.

    screen about():

        tag menu

        ## This use statement includes the game_menu screen inside this one. The
        ## vbox child is then included inside the viewport inside the game_menu
        ## screen.
        use game_menu(_("About"), scroll="viewport"):

            style_prefix "about"

            vbox:

                label "[config.name!t]"
                text _("Version [config.version!t]\n")

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


    ## This is redefined in options.rpy to add text to the about screen.
    define gui.about = ""


    style about_label is gui_label
    style about_label_text is gui_label_text
    style about_text is gui_text

    style about_label_text:
        size gui.label_text_size
init -1: ## Load and Save
    ## Load and Save screens #######################################################
    ##
    ## These screens are responsible for letting the player save the game and load
    ## it again. Since they share nearly everything in common, both are implemented
    ## in terms of a third screen, file_slots.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#save https://
    ## www.renpy.org/doc/html/screen_special.html#load


    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

        use game_menu(title):

            fixed:

                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                button:
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()


    style page_label is gui_label
    style page_label_text is gui_label_text
    style page_button is gui_button
    style page_button_text is gui_button_text

    style slot_button is gui_button
    style slot_button_text is gui_button_text
    style slot_time_text is slot_button_text
    style slot_name_text is slot_button_text

    style page_label:
        xpadding 75
        ypadding 5

    style page_label_text:
        text_align 0.5
        layout "subtitle"
        hover_color gui.hover_color

    style page_button:
        properties gui.button_properties("page_button")

    style page_button_text:
        properties gui.button_text_properties("page_button")

    style slot_button:
        properties gui.button_properties("slot_button")

    style slot_button_text:
        properties gui.button_text_properties("slot_button")
screen save():
    tag menu
    use file_slots(_("Save"))
screen load():
    tag menu
    use file_slots(_("Load"))
init -1: ## Preferences
    ## Preferences screen ##########################################################
    ##
    ## The preferences screen allows the player to configure the game to better suit
    ## themselves.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#preferences

    screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):

            vbox:

                hbox:
                    box_wrap True

                    if renpy.variant("pc"):

                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "radio"
                        label _("Rollback Side")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

                    vbox:
                        style_prefix "check"
                        label _("Skip Text")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                    vbox:
                        style_prefix "radio"
                        label _("Sakura Mode")
                        textbutton _("Disabled") action SetField(persistent, "sakura", 0)
                        textbutton _("Face Zoom In") action SetField(persistent, "sakura", 1)
                        textbutton _("Skip") action SetField(persistent, "sakura", 2)

                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:

                        label _("Text Speed")

                        bar value Preference("text speed")

                        label _("Auto-Forward Time")

                        bar value Preference("auto-forward time")

                    vbox:

                        if config.has_music:
                            label _("Music Volume")

                            hbox:
                                bar value Preference("music volume")

                        if config.has_sound:

                            label _("Sound Volume")

                            hbox:
                                bar value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)


    #                    if config.has_voice:
    #                        label _("Voice Volume")
    #
    #                        hbox:
    #                            bar value Preference("voice volume")
    #
    #                            if config.sample_voice:
    #                                textbutton _("Test") action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"


    style pref_label is gui_label
    style pref_label_text is gui_label_text
    style pref_vbox is vbox

    style radio_label is pref_label
    style radio_label_text is pref_label_text
    style radio_button is gui_button
    style radio_button_text is gui_button_text
    style radio_vbox is pref_vbox

    style check_label is pref_label
    style check_label_text is pref_label_text
    style check_button is gui_button
    style check_button_text is gui_button_text
    style check_vbox is pref_vbox

    style slider_label is pref_label
    style slider_label_text is pref_label_text
    style slider_slider is gui_slider
    style slider_button is gui_button
    style slider_button_text is gui_button_text
    style slider_pref_vbox is pref_vbox

    style mute_all_button is check_button
    style mute_all_button_text is check_button_text

    style pref_label:
        top_margin gui.pref_spacing
        bottom_margin 3

    style pref_label_text:
        yalign 1.0

    style pref_vbox:
        xsize 338

    style radio_vbox:
        spacing gui.pref_button_spacing

    style radio_button:
        properties gui.button_properties("radio_button")
        foreground "gui/button/radio_[prefix_]foreground.png"

    style radio_button_text:
        properties gui.button_text_properties("radio_button")

    style check_vbox:
        spacing gui.pref_button_spacing

    style check_button:
        properties gui.button_properties("check_button")
        foreground "gui/button/check_[prefix_]foreground.png"

    style check_button_text:
        properties gui.button_text_properties("check_button")

    style slider_slider:
        xsize 525

    style slider_button:
        properties gui.button_properties("slider_button")
        yalign 0.5
        left_margin 15

    style slider_button_text:
        properties gui.button_text_properties("slider_button")

    style slider_vbox:
        xsize 675
init -1: ## History (Transcript)
    ## History screen ##############################################################
    ##
    ## This is a screen that displays the dialogue history to the player. While
    ## there isn't anything special about this screen, it does have to access the
    ## dialogue history stored in _history_list.
    ##
    ## https://www.renpy.org/doc/html/history.html

    screen history():

        tag menu

        ## Avoid predicting this screen, as it can be very large.
        predict False

        use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

            style_prefix "history"

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")


    ## This determines what tags are allowed to be displayed on the history screen.

    define gui.history_allow_tags = set()


    style history_window is empty

    style history_name is gui_label
    style history_name_text is gui_label_text
    style history_text is gui_text

    style history_text is gui_text

    style history_label is gui_label
    style history_label_text is gui_label_text

    style history_window:
        xfill True
        ysize gui.history_height

    style history_name:
        xpos gui.history_name_xpos
        xanchor gui.history_name_xalign
        ypos gui.history_name_ypos
        xsize gui.history_name_width

    style history_name_text:
        min_width gui.history_name_width
        text_align gui.history_name_xalign

    style history_text:
        xpos gui.history_text_xpos
        ypos gui.history_text_ypos
        xanchor gui.history_text_xalign
        xsize gui.history_text_width
        min_width gui.history_text_width
        text_align gui.history_text_xalign
        layout ("subtitle" if gui.history_text_xalign else "tex")

    style history_label:
        xfill True

    style history_label_text:
        xalign 0.5
init -1: ## Help
    ## Help screen #################################################################
    ##
    ## A screen that gives information about key and mouse bindings. It uses other
    ## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
    ## help.

    screen help():

        tag menu

        default device = "keyboard"

        use game_menu(_("Help"), scroll="viewport"):

            style_prefix "help"

            vbox:
                spacing 23

                hbox:

                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help


    screen keyboard_help():

        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            label _("Escape")
            text _("Accesses the game menu.")

        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")

        hbox:
            label "H"
            text _("Hides the user interface.")

        hbox:
            label "S"
            text _("Takes a screenshot.")

        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


    screen mouse_help():

        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")

        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")

        hbox:
            label _("Mouse Wheel Up\nClick Rollback Side")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")


    screen gamepad_help():

        hbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")


        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")

        hbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")

        hbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")

        textbutton _("Calibrate") action GamepadCalibrate()


    style help_button is gui_button
    style help_button_text is gui_button_text
    style help_label is gui_label
    style help_label_text is gui_label_text
    style help_text is gui_text

    style help_button:
        properties gui.button_properties("help_button")
        xmargin 12

    style help_button_text:
        properties gui.button_text_properties("help_button")

    style help_label:
        xsize 375
        right_padding 30

    style help_label_text:
        size gui.text_size
        xalign 1.0
        text_align 1.0

################################################################################
## Flowchart (Custom)
################################################################################
init -2: ## Flowchart [variables]
    default persistent.flowspec = "com"
    default persistent.flowdrop = "none"
    image fanu = Image("flow_arr_null.png")
    image fatl = Image("flow_arr_tl.png")
    image fatm = Image("flow_arr_tm.png")
    image fatr = Image("flow_arr_tr.png")
    image fatx = Image("flow_arr_tx.png")
    image fabl = Image("flow_arr_bl.png")
    image fabm = Image("flow_arr_bm.png")
    image fabr = Image("flow_arr_br.png")
    image fabx = Image("flow_arr_bx.png")
init -1: ## Flowchart Page
    ## Flowchart Screen ################################################################
    ##
    ## This is a WIP screen for a route spreadsheet
    ##
    ## Original Source:   #Now heavily outdated
    ## https://www.reddit.com/r/RenPy/comments/flr39e/flowcharts_possible/
    screen flowchart():
        tag menu
        #label Text(_("Dev Scene Select"), size=120, xpos=0.5)
        use game_menu(_("Flowchart")):
            style_prefix "flowchart"
            add gui.game_menu_background
            use flowchart_navigation
            use flowchart_window
    style flowchart_hbox is hbox
    style flowchart_hbox:
        xalign 0.5
        #spacing gui.choice_spacing
    style flowchart_button is button
    style flowchart_button is default:
        xalign 0.5
        xsize 240
        #properties gui.button_properties("choice_button")
    style flowchart_button_text is button_text
    style flowchart_button_text is default:
        xalign 0.5
        xsize 240
        text_align 0.5
        #properties gui.button_text_properties("choice_button")
init -1: ## Flowchart Navigation
    screen flowchart_navigation():
        #zorder 1
        vbox:
            style_prefix "navigation"
            xpos 0.85
            ypos 0.05
            yanchor 0.0
            spacing gui.navigation_spacing
            textbutton _(" Developent")  action SetField(persistent, "flowspec", "dev")
            textbutton _(" Common")      action SetField(persistent, "flowspec", "com")
            if persistent.flowdrop == "none":
                textbutton _("MAIN")     action SetField(persistent, "flowdrop", "main")
                textbutton _("SIDE")     action SetField(persistent, "flowdrop", "side")
                textbutton _("EXTRA")    action SetField(persistent, "flowdrop", "extr")
            if persistent.flowdrop == "main":
                textbutton _("MAIN")     action SetField(persistent, "flowdrop", "none"):
                    text_color "#cc4444"
                textbutton _(" Geisha")  action SetField(persistent, "flowspec", "gei")
                textbutton _(" Haruka")  action SetField(persistent, "flowspec", "krn")
                textbutton _(" Kaori")   action SetField(persistent, "flowspec", "har")
                textbutton _(" Kirara")  action SetField(persistent, "flowspec", "krr")
                textbutton _(" Scotlyn") action SetField(persistent, "flowspec", "sco")
                textbutton _("SIDE")     action SetField(persistent, "flowdrop", "side")
                textbutton _("EXTRA")    action SetField(persistent, "flowdrop", "extr")
            if persistent.flowdrop == "side":
                textbutton _("MAIN")     action SetField(persistent, "flowdrop", "main")
                textbutton _("SIDE")     action SetField(persistent, "flowdrop", "none"):
                    text_color "#cc4444"
                textbutton _(" Brandon") action SetField(persistent, "flowspec", "bra")
                textbutton _(" Brianne") action SetField(persistent, "flowspec", "bri")
                textbutton _(" Fumika")  action SetField(persistent, "flowspec", "fum")
                textbutton _(" Nekome")  action SetField(persistent, "flowspec", "nek")
                textbutton _(" Shoko")   action SetField(persistent, "flowspec", "sho")
                textbutton _(" Rin")     action SetField(persistent, "flowspec", "rin")
                textbutton _(" Toge")    action SetField(persistent, "flowspec", "tog")
                textbutton _(" Shio")    action SetField(persistent, "flowspec", "shi")
                textbutton _("EXTRA")    action SetField(persistent, "flowdrop", "extr")
            elif persistent.flowdrop == "extr":
                textbutton _("MAIN")     action SetField(persistent, "flowdrop", "main")
                textbutton _("SIDE")     action SetField(persistent, "flowdrop", "side")
                textbutton _("EXTRA")    action SetField(persistent, "flowdrop", "none"):
                    text_color "#cc4444"
                textbutton _(" Yuri")    action SetField(persistent, "flowspec", "yuri")
                textbutton _(" Harem")   action SetField(persistent, "flowspec", "harm")
init -1: ## Flowchart Window
    screen flowchart_window():
        style_prefix "flowchart"
        frame:
            xsize 1080
            xalign 0.0
            ysize 720
            yalign 0.0
            has side "c r b"
            if   persistent.flowspec == "dev":
                use flowchart_w_dev
            elif persistent.flowspec == "gei":
                use flowchart_w_gei
            elif persistent.flowspec == "krn":
                use flowchart_w_krn
            elif persistent.flowspec == "har":
                use flowchart_w_har
            elif persistent.flowspec == "krr":
                use flowchart_w_krr
            elif persistent.flowspec == "sco":
                use flowchart_w_sco
            elif persistent.flowspec == "bra":
                use flowchart_w_bra
            elif persistent.flowspec == "bri":
                use flowchart_w_bri
            elif persistent.flowspec == "fum":
                use flowchart_w_fum
            elif persistent.flowspec == "nek":
                use flowchart_w_nek
            elif persistent.flowspec == "shi":
                use flowchart_w_shi
            elif persistent.flowspec == "sho":
                use flowchart_w_sho
            elif persistent.flowspec == "rin":
                use flowchart_w_rin
            elif persistent.flowspec == "tog":
                use flowchart_w_tog
            else: # persistent.flowspec == "com"
                use flowchart_w_com
    ## Flowcharts By Route:
    screen flowchart_w_dev:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1080
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("Start") action Jump("start")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Dev Menu") action Jump("devmen")
                vbox:
                    xalign 0.5
                    hbox:
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                        #image fanu
                        #textbutton _("Prologue Intro")
                        #image
                hbox:
                    xsize 200
                    textbutton _("Prologue Intro") action Jump("prologue_intr")
                    null width 240
                    textbutton _("Prologue Q&A") action Jump("prologue_qna")
                textbutton _("Prologue Concert End") action Jump("prologue_concert_end")
                textbutton _("Sakura Mode \nExplanation") action Jump("experimental")
                textbutton _("Demo H Scene") action Jump("demo_h_start")
                textbutton _("End Of WIP") action NullAction()

                grid 3 3:
                    xalign 0.5
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_com:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_gei:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                vbox: ## Act 1 - Detention
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_nx.png"
                    add "gui/flar_nx.png"
                    textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Detention") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Talk To Haruka") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Follow Geisha") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Hear Weird Noises In The Bathroom") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Go Into The Mens Bathroom") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Bathroom Glory"):
                        text_color "#f377d1"
                        #action Jump("script_label")
                vbox: ## Act 2 - Run in With Violet
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Run-In With Violet") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Leave Her With Oda") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Take Geisha Home") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Hidden Functions") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Cheering Flowers") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Invite Geisha Out") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Runaway Gal") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Love Dove Gyaru") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tlx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        textbutton _("A Rough Quickie"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                        textbutton _("Back Alley Shag"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_brx.png"
                        add "gui/flar_nx.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                vbox: ## Act 3 - Fly Me To The Moon
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    textbutton _("Fly Me To The Moon") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Let Me Play Amongst The Stars") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Idol Date Plans") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    textbutton _("Fill My Heart With Song") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Corporate Brats") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Corporate Sponsor") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Old Frenemies New Idol") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Never Meet Your Idol") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("You Are All I Long For") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("All I Worship And Adore") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("In Other Words, Please Be True") #action Jump("script_label")
                vbox: ## Act 4 - An Idol Over For Dinner
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("An Idol Over For Dinner")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Father My Way") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Geisha's Bedroom") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Deal With \nThe Devil") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("A Gyaru Begs Her Idol") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("The Star \nLost Its \nShine") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Scotlyn Shines Brighter") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_trx.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        textbutton _("My Way") #action Jump("script_label")
                        textbutton _("Come Fly With Me") #action Jump("script_label")
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_brx.png"
                        add "gui/flar_nx.png"
                    textbutton _("Cheerleader ##### Fight") #action Jump("script_label")
                vbox: ## Act 5 - Goon Squad, Make Or Break
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_tx.png":
                        xalign 0.5
                    textbutton _("Ask Haruka For Advice On The Goon Squad") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("BOOBS... *Sigh* You Had One Job") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Endurance Of The Mind") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Spend The Day With Nekome") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Nekome Owes Geisha For Everything") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Comfort Nekome, It's Ok To Be Angry") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Spend The Day With Atsuko") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tmx.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        yalign 0.5
                        textbutton _("Who Are You Again... \nMy Pet?") #action Jump("script_label")
                        textbutton _("Talk \nTo \nScotlyn") #action Jump("script_label")
                        textbutton _("Acknowledge Atsuko") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_tx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bmx.png"
                        add "gui/flar_tl.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Go To Geisha's House") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("She Did Nothing Wrong") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("She ####ed Up... Help A Goon Out") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bm.png"
                        add "gui/flar_tl.png"
                vbox: ## Act 6 - Goon Squad Conclusion
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("G-Day") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tmx.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_hx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_hx.png"
                    hbox:
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                        textbutton _("Musical Guidence") #action Jump("script_label")
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_hx.png"
                        add "gui/flar_tx.png"
                        add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_blx.png"
                        add "gui/flar_tm.png"
                        add "gui/flar_brx.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Gal Massacre") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Gal Confrontation") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Speaking Her Mind Killed The Cat ") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("Chat To The Pets") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Death Of The Squad") #action Jump("script_label")
                        add "gui/flar_nx.png"
                        textbutton _("A ##### Slapped") #action Jump("script_label")
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        add "gui/flar_trx.png"
                        add "gui/flar_br.png"
                        add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_hx.png"
                        add "gui/flar_hx.png"
                    hbox:
                        textbutton _("Mayoral Obligations") #action Jump("script_label")
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_hx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Secret Informant") #action Jump("script_label")
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                        textbutton _("A Catty \nThreesome"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_hx.png"
                        add "gui/flar_tx.png"
                    hbox:
                        textbutton _("Heir The Sky") #action Jump("script_label")
                        add "gui/flar_hx.png"
                        add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_hx.png"
                        add "gui/flar_hx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_bmx.png"
                        add "gui/flar_tl.png"
                vbox: ## Act 7 - The Oda Strikes Back!
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Scandelous Behaviour") #action Jump("script_label")
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("An Incel With A Grudge") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tlx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        textbutton _("Suffocations A #####"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                        textbutton _("Tactical #######"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tx.png"
                        add "gui/flar_tx.png"
                        add "gui/flar_nx.png"
                    hbox:
                        add "gui/flar_tr.png"
                        add "gui/flar_brx.png"
                        add "gui/flar_nx.png"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Skeleton Filled Closet") #action Jump("script_label")
                vbox: ## Act 8 - Gyaru Merchandice Sold
                    xalign 0.5
                    xsize 1280
                    style_prefix "flowchart"
                    add "gui/flar_bx.png":
                        xalign 0.5
                    textbutton _("Gyaru Merchandice Sold") #action Jump("script_label")
                    add "gui/flar_tx.png":
                        xalign 0.5
                    hbox:
                        add "gui/flar_bl.png"
                        add "gui/flar_tmx.png"
                        add "gui/flar_br.png"
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_hx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("Family Over Friends") #action Jump("script_label")
                        vbox:
                            add "gui/flar_hx.png"
                            add "gui/flar_hx.png"
                        textbutton _("#### THE PARENTS") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("A Bad Ride"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                        textbutton _("Disowned") #action Jump("script_label")
                        textbutton _("Beat Up The Incel") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        textbutton _("A Cat To The Rescue") #action Jump("script_label")
                        textbutton _("The Goons Are Back In Town") #action Jump("script_label")
                        textbutton _("Family Fortune") #action Jump("script_label")
                    hbox:
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                        add "gui/flar_bx.png"
                    hbox:
                        vbox:
                            textbutton _("Queen Of \nThe Pole") #action Jump("script_label")
                            add "gui/flar_tx.png"
                            add "gui/flar_hx.png"
                        vbox:
                            textbutton _("My Kind \nOf Town") #action Jump("script_label")
                            add "gui/flar_tx.png"
                            add "gui/flar_hx.png"
                        textbutton _("The ###### To End All #######"):
                            text_color "#f377d1"
                            #action Jump("script_label")
                    hbox:
                        vbox:
                            xalign 0.5
                            add "gui/flar_bx.png"
                            textbutton _("Bad \nEnd"):
                                text_color "#ff8888"
                                xalign 0.5
                        vbox:
                            xalign 0.5
                            add "gui/flar_bx.png"
                            textbutton _("Neutral \nEnd"):
                                text_color "#ffff88"
                                xalign 0.5
                        vbox:
                            xalign 0.5
                            add "gui/flar_bx.png"
                            textbutton _("Good \nEnd"):
                                text_color "#88ff88"
                                xalign 0.5
                    add "gui/flar_nx.png"
                    add "gui/flar_nx.png"
    screen flowchart_w_krn:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_har:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_krr:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_sco:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_bra:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_bri:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_fum:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_nek:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_sho:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_rin:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_tog:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"
    screen flowchart_w_shi:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            xsize 1080
            xalign 0.5
            vbox:
                xalign 0.5
                xsize 1280
                style_prefix "flowchart"
                add "gui/flar_nx.png"
                textbutton _("{i}Common Route{/i}") action SetField(persistent, "flowspec", "com")
                add "gui/flar_bx.png":
                    xalign 0.5
                textbutton _("Scene_Name") #action Jump("script_label")
                add "gui/flar_tx.png":
                    xalign 0.5
                hbox:
                    add "gui/flar_bl.png"
                    add "gui/flar_tm.png"
                    add "gui/flar_br.png"
                hbox:
                    add "gui/flar_tx.png"
                    add "gui/flar_nx.png"
                    add "gui/flar_bx.png"
                hbox:
                    add "gui/flar_tr.png"
                    add "gui/flar_bm.png"
                    add "gui/flar_tl.png"

################################################################################
## Additional screens
################################################################################
init -1: ## Confirm
    ## Confirm screen ##############################################################
    ##
    ## The confirm screen is called when Ren'Py wants to ask the player a yes or no
    ## question.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#confirm

    screen confirm(message, yes_action, no_action):

        ## Ensure other screens do not get input while this screen is displayed.
        modal True

        zorder 200

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action

        ## Right-click and escape answer "no".
        key "game_menu" action no_action


    style confirm_frame is gui_frame
    style confirm_prompt is gui_prompt
    style confirm_prompt_text is gui_prompt_text
    style confirm_button is gui_medium_button
    style confirm_button_text is gui_medium_button_text

    style confirm_frame:
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5

    style confirm_prompt_text:
        text_align 0.5
        layout "subtitle"

    style confirm_button:
        properties gui.button_properties("confirm_button")

    style confirm_button_text:
        properties gui.button_text_properties("confirm_button")
init -1: ## Skip Indicator
    ## Skip indicator screen #######################################################
    ##
    ## The skip_indicator screen is displayed to indicate that skipping is in
    ## progress.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

    screen skip_indicator():

        zorder 100
        style_prefix "skip"

        frame:

            hbox:
                spacing 9

                text _("Skipping")

                text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


    ## This transform is used to blink the arrows one after another.
    transform delayed_blink(delay, cycle):
        alpha .5

        pause delay

        block:
            linear .2 alpha 1.0
            pause .2
            linear .2 alpha 0.5
            pause (cycle - .4)
            repeat


    style skip_frame is empty
    style skip_text is gui_text
    style skip_triangle is skip_text

    style skip_frame:
        ypos gui.skip_ypos
        background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
        padding gui.skip_frame_borders.padding

    style skip_text:
        size gui.notify_text_size

    style skip_triangle:
        ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
        ## glyph in it.
        font "DejaVuSans.ttf"
init -1: ## Notify
    ## Notify screen ###############################################################
    ##
    ## The notify screen is used to show the player a message. (For example, when
    ## the game is quicksaved or a screenshot has been taken.)
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#notify-screen

    screen notify(message):

        zorder 100
        style_prefix "notify"

        frame at notify_appear:
            text "[message!tq]"

        timer 3.25 action Hide('notify')


    transform notify_appear:
        on show:
            alpha 0
            linear .25 alpha 1.0
        on hide:
            linear .5 alpha 0.0


    style notify_frame is empty
    style notify_text is gui_text

    style notify_frame:
        ypos gui.notify_ypos

        background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
        padding gui.notify_frame_borders.padding

    style notify_text:
        properties gui.text_properties("notify")
init -1: ## NVL
    ## NVL screen ##################################################################
    ##
    ## This screen is used for NVL-mode dialogue and menus.
    ##
    ## https://www.renpy.org/doc/html/screen_special.html#nvl


    screen nvl(dialogue, items=None):

        window:
            style "nvl_window"

            has vbox:
                spacing gui.nvl_spacing

            ## Displays dialogue in either a vpgrid or the vbox.
            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


    screen nvl_dialogue(dialogue):

        for d in dialogue:

            window:
                id d.window_id

                fixed:
                    yfit gui.nvl_height is None

                    if d.who is not None:

                        text d.who:
                            id d.who_id

                    text d.what:
                        id d.what_id

    ## This controls the maximum number of NVL-mode entries that can be displayed at
    ## once.
    define config.nvl_list_length = gui.nvl_list_length

    style nvl_window is default
    style nvl_entry is default

    style nvl_label is say_label
    style nvl_dialogue is say_dialogue

    style nvl_button is button
    style nvl_button_text is button_text

    style nvl_window:
        xfill True
        yfill True

        background "gui/nvl.png"
        padding gui.nvl_borders.padding

    style nvl_entry:
        xfill True
        ysize gui.nvl_height

    style nvl_label:
        xpos gui.nvl_name_xpos
        xanchor gui.nvl_name_xalign
        ypos gui.nvl_name_ypos
        yanchor 0.0
        xsize gui.nvl_name_width
        min_width gui.nvl_name_width
        text_align gui.nvl_name_xalign

    style nvl_dialogue:
        xpos gui.nvl_text_xpos
        xanchor gui.nvl_text_xalign
        ypos gui.nvl_text_ypos
        xsize gui.nvl_text_width
        min_width gui.nvl_text_width
        text_align gui.nvl_text_xalign
        layout ("subtitle" if gui.nvl_text_xalign else "tex")

    style nvl_thought:
        xpos gui.nvl_thought_xpos
        xanchor gui.nvl_thought_xalign
        ypos gui.nvl_thought_ypos
        xsize gui.nvl_thought_width
        min_width gui.nvl_thought_width
        text_align gui.nvl_thought_xalign
        layout ("subtitle" if gui.nvl_text_xalign else "tex")

    style nvl_button:
        properties gui.button_properties("nvl_button")
        xpos gui.nvl_button_xpos
        xanchor gui.nvl_button_xalign

    style nvl_button_text:
        properties gui.button_text_properties("nvl_button")

################################################################################
## Mobile Variants
################################################################################
init -1: ## Mobile
    style pref_vbox:
        variant "medium"
        xsize 675

    ## Since a mouse may not be present, we replace the quick menu with a version
    ## that uses fewer and bigger buttons that are easier to touch.
    screen quick_menu():
        variant "touch"

        zorder 100

        if quick_menu:

            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 1.0

                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Menu") action ShowMenu()


    style window:
        variant "small"
        background "gui/phone/textbox.png"

    style radio_button:
        variant "small"
        foreground "gui/phone/button/radio_[prefix_]foreground.png"

    style check_button:
        variant "small"
        foreground "gui/phone/button/check_[prefix_]foreground.png"

    style nvl_window:
        variant "small"
        background "gui/phone/nvl.png"

    style main_menu_frame:
        variant "small"
        background "gui/phone/overlay/main_menu.png"

    style game_menu_outer_frame:
        variant "small"
        background "gui/phone/overlay/game_menu.png"

    style game_menu_navigation_frame:
        variant "small"
        xsize 510

    style game_menu_content_frame:
        variant "small"
        top_margin 0

    style pref_vbox:
        variant "small"
        xsize 600

    style bar:
        variant "small"
        ysize gui.bar_size
        left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

    style vbar:
        variant "small"
        xsize gui.bar_size
        top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

    style scrollbar:
        variant "small"
        ysize gui.scrollbar_size
        base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

    style vscrollbar:
        variant "small"
        xsize gui.scrollbar_size
        base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style slider:
        variant "small"
        ysize gui.slider_size
        base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

    style vslider:
        variant "small"
        xsize gui.slider_size
        base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

    style slider_pref_vbox:
        variant "small"
        xsize None

    style slider_pref_slider:
        variant "small"
        xsize 900

##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################
