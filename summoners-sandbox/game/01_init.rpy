python early:   
    
    expressions = [ 
        'default'
        'sigh',
        'shout',
        'roar',
        'flinch',
        'laugh',
        'sob',
        'sniff'
        ]
    
    filetypes = {
        'sound' : '.wav',
        }
    
    
    class Deamon:
        succubus = 0
        zombie = 1
        frank_sinatra = 2
        
        
        head = None
        torso = None
        legs = None
        
        _expression = ''
        
        def __init__(head, torso, legs):
            self.head = head
            self.torso = torso
            self.legs = legs
            
        def set_expression(expression):
            self._expression = expression
            
            Play("sound", self._expression + filetypes['sound'])
            # TODO : PLAY ONE SOUND AT A TIME?
            
    
    def to_expression(name):
        return '*' + name + '*'
    
    def parse_smartline(lex):        
        global sounds, expressions
        
        who = lex.simple_expression()
        what = lex.rest().strip('"' + "'")
        
        for expression in expressions:
            if to_expression(expression) in what:
                pass
                
        return (who, what)

    def execute_smartline(o):
        global variable
        
        who, what = o
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
    
    summoned_deamon = None