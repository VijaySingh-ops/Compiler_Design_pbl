def semantic_analysis(tokens, language):
    if language == "python":
        if ('KEYWORD', 'def') in tokens and ('KEYWORD', 'return') not in tokens:
            return "Warning: Function with no return"
    if language == "java":
        if ('KEYWORD', 'void') in tokens and ('SYMBOL', ';') not in tokens:
            return "Semantic Error: Missing semicolon"
    if language == "c":
        if ('KEYWORD', 'int') in tokens and ('KEYWORD', 'return') not in tokens:
            return "Semantic Error: 'main' must return a value"
    return "Semantics are OK"
