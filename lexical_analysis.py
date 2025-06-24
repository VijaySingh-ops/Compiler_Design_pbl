import re

def lexical_analysis(code, language):
    tokens = []
    keyword_map = {
        "python": ['def', 'print', 'if', 'else', 'import', 'return', 'while', 'for', 'in'],
        "c": ['int', 'float', 'main', 'printf', '#include', 'return', 'if', 'else', 'for', 'while']
    }
    split_code = re.findall(r'\w+|[^\s\w]', code)
    for word in split_code:
        if word in keyword_map.get(language.lower(), []):
            tokens.append(('KEYWORD', word))
        elif word.isdigit():
            tokens.append(('NUMBER', word))
        elif word in ['(', ')', '{', '}', '=', ';', ',', '.', '"', ':']:
            tokens.append(('SYMBOL', word))
        elif word.isidentifier():
            tokens.append(('IDENTIFIER', word))
        else:
            tokens.append(('UNKNOWN', word))
    return tokens
