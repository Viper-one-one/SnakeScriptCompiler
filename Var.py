import Token

class Var(Token):
    
    def __init__(self, value):
        pass
    
    def __eq__(self, other):
        return isinstance(self, other)
    
    def __str__(self):
        return "Var"
    
    def __hash__(self):
        return 5