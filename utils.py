def detect_language(code):
    if 'def' in code or 'print' in code:
        return "python"
    elif '#include' in code or 'main' in code or 'int' in code:
        return "c"
    return "unknown"

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return ""