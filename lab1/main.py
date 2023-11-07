import scanner

if __name__ == "__main__":
    lexer = scanner.lexer
    fh = open("example_full.txt", "r")
    lexer.input( fh.read() )
    print(scanner.tokens)
    for token in lexer:
        print(f"line %d: %s(%s)" %(token.lineno, token.type, token.value))