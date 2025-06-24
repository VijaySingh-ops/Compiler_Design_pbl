import dis
import tempfile

def code_generation(tokens, language, user_code=""):
    if language == "python":
        try:
            compiled = compile(user_code, "<string>", "exec")
            bytecode = dis.Bytecode(compiled)
            lines = [f"{instr.opname} {instr.argrepr}" for instr in bytecode]
            return "\n".join(lines)
        except Exception as e:
            return f"Bytecode generation failed: {str(e)}"

    elif language == "c":
        lines = []
        for t in tokens:
            if t[0] == 'IDENTIFIER':
                lines.append(f"LOAD {t[1]}")
            elif t[0] == 'NUMBER':
                lines.append(f"PUSH {t[1]}")
            elif t[0] == 'KEYWORD' and t[1] == 'return':
                lines.append("RET")
        return "\n".join(lines) if lines else ">>> Simulated C Assembly"

    return ">>> Code generation failed"
