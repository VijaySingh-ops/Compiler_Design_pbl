import tkinter as tk
from tkinter import filedialog, messagebox
from backend.utils import detect_language, read_file
from backend.lexical_analysis import lexical_analysis
from backend.syntax_analysis import syntax_analysis
from backend.semantic_analysis import semantic_analysis
from backend.code_generation import code_generation
from PIL import Image, ImageTk
import os

class CustomCompilerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student-Made Mini Compiler")
        self.root.geometry("1024x720")
        self.root.configure(bg="#f0f0f0")

        self.code_area = tk.Text(root, height=18, width=100, font=("Consolas", 11), bg="#ffffff")
        self.code_area.pack(pady=10)

        controls = tk.Frame(root, bg="#f0f0f0")
        controls.pack()

        tk.Button(controls, text="Load Code", command=self.load_code, bg="#007acc", fg="white", width=12).pack(side="left", padx=10)
        tk.Button(controls, text="Compile", command=self.compile_code, bg="#28a745", fg="white", width=12).pack(side="left", padx=10)
        tk.Button(controls, text="View Parse Tree", command=self.view_parse_tree, bg="#6c757d", fg="white", width=14).pack(side="left", padx=10)
        tk.Button(controls, text="Clear", command=self.clear_code, bg="#dc3545", fg="white", width=10).pack(side="left", padx=10)

        self.output_area = tk.Text(root, height=10, width=100, font=("Courier", 10), bg="#f9f9f9")
        self.output_area.pack(pady=10)

        tk.Label(root, text="Made by Student | 2025 Project", bg="#f0f0f0", fg="#999").pack(pady=5)

    def load_code(self):
        path = filedialog.askopenfilename(filetypes=[("Code Files", "*.py *.c *.java *.txt")])
        if path:
            code = read_file(path)
            self.code_area.delete("1.0", tk.END)
            self.code_area.insert("1.0", code)

    def compile_code(self):
        code = self.code_area.get("1.0", tk.END).strip()
        if not code:
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert("1.0", "Please enter or load code to compile.")
            return

        language = detect_language(code)
        tokens = lexical_analysis(code, language)
        syntax_result = syntax_analysis(tokens, language)
        semantic_result = semantic_analysis(tokens, language)
        code_result = code_generation(tokens, language)

        output = f"Language: {language}\n\n"
        output += f"Lexical Tokens:\n{tokens}\n\n"
        output += f"Syntax: {syntax_result}\n"
        output += f"Semantic: {semantic_result}\n"
        output += f"Code Generation:\n{code_result}\n"

        self.output_area.delete("1.0", tk.END)
        self.output_area.insert("1.0", output)

    def view_parse_tree(self):
        path = "output/parse_tree.png"
        if os.path.exists(path):
            top = tk.Toplevel(self.root)
            top.title("Parse Tree")
            img = Image.open(path)
            img = img.resize((600, 400))
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(top, image=photo)
            label.image = photo
            label.pack()
        else:
            messagebox.showerror("Error", "Parse tree not generated yet.")

    def clear_code(self):
        self.code_area.delete("1.0", tk.END)
        self.output_area.delete("1.0", tk.END)
