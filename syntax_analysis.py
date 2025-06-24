from .tree_generator import build_parse_tree

def syntax_analysis(tokens, language):
    rules = []
    token_values = [t[1] for t in tokens]

    if language == "python":
        if 'def' in token_values:
            rules.append("FunctionDef → def IDENTIFIER ( ) : BODY")
        if 'if' in token_values and 'else' in token_values:
            rules.append("Conditional → if CONDITION : BLOCK else : BLOCK")
        if 'for' in token_values:
            rules.append("Loop → for IDENTIFIER in RANGE : BLOCK")
        if 'while' in token_values:
            rules.append("Loop → while CONDITION : BLOCK")
        if 'print' in token_values:
            rules.append("PrintStmt → print ( VALUE )")

    elif language == "c":
        if 'main' in token_values:
            rules.append("MainDef → int main ( ) { BODY }")
        if 'int' in token_values and any(sym for sym in token_values if sym == ';'):
            rules.append("VarDecl → int IDENTIFIER = VALUE ;")
        if 'printf' in token_values:
            rules.append("PrintStmt → printf ( STRING ) ;")
        if 'return' in token_values:
            rules.append("ReturnStmt → return VALUE ;")
        if 'if' in token_values:
            rules.append("Conditional → if ( CONDITION ) { BLOCK }")
        if 'for' in token_values:
            rules.append("Loop → for ( INIT ; COND ; INCR ) { BLOCK }")
        if 'while' in token_values:
            rules.append("Loop → while ( CONDITION ) { BLOCK }")

    if rules:
        build_parse_tree(rules[0], "output/parse_tree.png")
        return f"Syntax OK. Matched: {rules[0]}"
    
    return "Syntax Error: No matching rules."
