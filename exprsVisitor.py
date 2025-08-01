from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

# Extiende la clase generada por ANTLR
class EvalVisitor(exprsVisitor):

    # Visit root node
    def visitRoot(self, ctx: exprsParser.RootContext):
        return self.visit(ctx.expr())

    # Visit number node
    def visitNumero(self, ctx: exprsParser.NumeroContext):
        # Convierte el token NUM a un número entero
        return int(ctx.NUM().getText())

    # Visit addition and subtraction
    def visitSumres(self, ctx: exprsParser.SumresContext):
        left = self.visit(ctx.expr(0))  # Lado izquierdo
        right = self.visit(ctx.expr(1))  # Lado derecho
        operator = ctx.getChild(1).getText()  # '+' o '-'
        if operator == '+':
            return left + right
        else:
            return left - right

    # Visit multiplication and division
    def visitMuldiv(self, ctx: exprsParser.MuldivContext):
        left = self.visit(ctx.expr(0))  # Lado izquierdo
        right = self.visit(ctx.expr(1))  # Lado derecho
        operator = ctx.getChild(1).getText()  # '*' o '/'
        if operator == '*':
            return left * right
        else:
            return left / right


input_stream = FileStream("texto.txt")
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

print("Árbol de sintaxis:", tree.toStringTree(recog=parser))
visitor = EvalVisitor()
result = visitor.visit(tree)

print("Resultado:", result)