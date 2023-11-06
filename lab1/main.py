import scaner

if __name__ == "__main__":
    lexer = scaner.lexer
    fh = open("lab1\example_full.txt", "r")
    lexer.input( fh.read() )
    print(scaner.tokens)
    for token in lexer:
        print(f"line %d: %s(%s)" %(token.lineno, token.type, token.value))