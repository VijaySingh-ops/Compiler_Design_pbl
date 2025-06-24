from graphviz import Digraph

def build_parse_tree(rule, output_path):
    dot = Digraph()
    rule = rule.replace("->", "→")
    lhs, rhs = rule.split("→")
    dot.node("A", lhs.strip())
    rhs_parts = rhs.strip().split()
    for i, part in enumerate(rhs_parts):
        dot.node(f"B{i}", part)
        dot.edge("A", f"B{i}")
    dot.render(output_path.replace(".png", ""), format='png', cleanup=True)
