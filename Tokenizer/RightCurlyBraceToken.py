from Tokenizer import Token

class RightCurlyBraceToken(Token):

    def __eq__(self, other):
        return isinstance(other, RightCurlyBraceToken)

    def __str__(self):
        return "RightCurlyBraceToken"

    def __hash__(self):
        return 22
