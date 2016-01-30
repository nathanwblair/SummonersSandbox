define e = Character(_('Eileen'), color="#c8ffc8")

label start:
    e "The garish crimson font seemed to stare at you, a shroud of foreboding closing"
    e "around you from all directions of your sacred space. There was no darkness akin" 
    e "to that sense of impending doom, the ticking hands of time a countdown to eventual" 
    e "and inevitable suffering."
    line e "Would you b*sigh*elieve in magic if it could save you from a miserable, lonely fate?"
    
    menu:
        "For the Joy, For the Fun, For the Life, I Shalt Live" if True:
           $ ""
           jump end_other_menu
        "For the Pain, For the Wrath, *sigh* For the Vengance, I Shalt Stand" if True:
           $ ""
           jump end_menu
            
    
        
    label end_menu:
        line "test"
    label end_other_menu:
        "memes"S