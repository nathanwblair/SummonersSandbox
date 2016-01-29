

define e = Character(_('Eileen'), color="#c8ffc8")

label start:
    
    line e "These quotes will show up, and don't need to be backslashed."
    
    menu:
        "For the Joy, For the Fun, For the Life, I Shalt Live" if True:
            $ ""
            jump end_other_menu
        "For the Pain, For the Wrath, For the Vengance, I Shalt Stand" if True:
            $ ""
            jump end_menu
        
    label end_menu:
        "test"
    label end_other_menu:
        "memes"