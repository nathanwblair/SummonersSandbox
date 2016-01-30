python early:       
    expressions = [ 
        'default',
        'sigh',
        'shout',
        'roar',
        'flinch',
        'laugh',
        'sob',
        'sniff',
        ]
    
    filetypes = {
            'sound' : '.ogg',
            'image' : '.png'
        }
    
    
    class Deamon: 
        name = ''
        
        lst_species = ['succubus',
                'zucherburg',
                'ibm salesman']
    
        character = Character(name, who_color="#c8ffc8")
        species = ''
        image_names = []
        
        _expression = ''
        
        
        def __init__(self, species):
            if species not in self.lst_species:
                raise ValueError('Species does not exist')
            self.species = species
            
            self._load_images()
        
        
        def _load_images(self):
            global expressions, filetypes
            
            species_path = 'images/' + self.species
            
            for expression in expressions:
                self.__load_image(species_path, expression)
            
        
        def __load_image(self, path, name):
            filename = path + '/' + name + filetypes['image']
            
            renpy.image(name, filename)
            
            self.image_names.append(name)         
        
        
        def set_expression(self, expression):
            self._expression = expression
            
            sound_path = 'sounds/' + self.species + '/' + self._expression + filetypes['sound']
            renpy.music.play(sound_path, channel='sound')

            self._set_expression_image(expression)

            
        def _set_expression_image(self, expression):
            renpy.show(expression)
            
            
    
    def to_expression(name):
        return '*' + name + '*'
    
    
    def parse_smartline(lex):      
        global sounds, expressions
        
        current_expression = None
        
        who = lex.simple_expression()
        what = lex.rest().strip('"' + "'")
        
                
        return (who, what)


    def execute_smartline(o):
        global variable, summoned_deamon
        
        who, what = o
        
        current_expression = None
        
        for expression in expressions:
            if what.find(to_expression(expression)) != -1:
                current_expression = expression
                
        if current_expression is not None:
            summoned_deamon.set_expression('sigh')

        renpy.say(eval(who), what)
        

    def lint_smartline(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)

    renpy.register_statement("line", parse=parse_smartline, execute=execute_smartline, lint=lint_smartline)
    
    summoned_deamon = Deamon('succubus')