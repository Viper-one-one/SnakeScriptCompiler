from Tokenizer import Token

class BreakToken(Token):
    
    def __eq__(self, other):
        return isinstance(other, BreakToken)
    
    def __str__():
        return "BreakToken"
    
    def __hash__(self):
        return 3