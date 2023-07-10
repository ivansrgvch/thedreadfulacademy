# Игра начинается здесь:
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character('[ggname]', color="#c8ffc8", image="doctor")
define da = False
define net = False 
define audio.trambon = 'audio/sounds/trambon.ogg'
define audio.rain = 'audio/sounds/rain.ogg'
define audio.ambient = 'audio/sounds/ambient5.ogg'
define dom = 0
define sub = 0
define charisma = 0
define intelligence = 0






# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
init:
    $ right1 = Position(xalign=1.5, yalign=0.1)
    $ left1 = Position(xalign=-1, yalign=1)


label splashscreen:
        scene preview

        with fade

        pause 3

        scene preview1

        with fade

        pause 3

return




label start:

    scene bg medical
    with fade
    
   

    
    stop music fadeout 3.0
    play music ambient
     

    $ ggname = renpy.input("Как вас зовут?", length=12, default="Sean", allow='qwertyuiopasdfghjkzxcvbnm-йцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKZXCVBNM-ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ').strip()

    if ggname == '':
        $ ggname = "Sean"


        

    

    show doctor smile at left1
    with fade

    
    a "Привет"
        
    show doctor at left1

    a "Привет"

    a @ smile "Сосать будешь?  {w=1}Я имею ввиду хуй."
    
    a "Ах ты сука"
    
    scene bg police
    
    show doctor at right1

    a "Ну так что?"

    hide doctor
    with dissolve

    menu:
        "да":
            $ sub += 1     

            $ da = True
            
            $ renpy.notify("Он запомнит это")
            


            jump vibor1

        "нет":
            $ dom += 1
            
            $ net = True

            $ renpy.notify("Он запомнит это")
            

            jump virob2


label vibor1:
    

    a "да."

    "ты согласился сосать"
    
    
    if da:
        a "открывай рот"


    if net:
        a "ну и пошел нахуй"

    jump ulica

    return

label virob2:
    

    a "нет"

    "ты отказался сосать"
        
        
    if da:
        a "открывай рот"

    if net:
        a "ну и пошел нахуй"

        play sound trambon


        
        
       
        

    jump ulica

    
    
    

    return

label ulica:


    
    scene bg ulica
    with fade

    play music rain

    show doctor at left1
    with fade

    if da:
        "Ты сосал два часа и на улице уже стемнело"

    if net:
        "На улице уже стемнело"

    menu:
        "да":
            "выа"
        "нет" if dom == 1:
            "sfhg"
        "хвй"  if dom == 2:
            "fshgsdfhg"

        
    
            

        
        

        

    return


