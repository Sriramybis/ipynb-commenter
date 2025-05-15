import json
from pathlib import Path
from typing import List

from nbformat import read, write, NO_CONVERT, NotebookNode
from nbformat.v4 import new_markdown_cell
import requests
import os

def read_notebook(path: str) -> NotebookNode:
    print(f"📘 Reading notebook from {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        return read(f, as_version=4)

def generate_markdown(title: str, subtitle: str, explanation: str) -> str:
    return f"""# {title}
## {subtitle}
{explanation}"""

def infer_commentary(code: str, index: int) -> str:
    """
    Use Ollama to generate markdown commentary for the code cell.
    """
    print(f"→ Sending code block {index + 1} to LLM for explanation...")
    prompt = f"""
Given the following Python code block, generate a markdown explanation in the following format:
# Title
## Sub title
Explanation

Code:
{code}
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        if response.status_code == 200:
            print(f"✓ Received response for block {index + 1}")
            return response.json().get('response', generate_markdown("Code Block", f"Step {index + 1}", "No response from LLM."))
        else:
            print(f"✗ Failed to get response for block {index + 1}: HTTP {response.status_code}")
            return generate_markdown("Code Block", f"Step {index + 1}", f"LLM request failed with status {response.status_code}.")
    except Exception as e:
        print(f"✗ Exception during LLM request for block {index + 1}: {str(e)}")
        return generate_markdown("Code Block", f"Step {index + 1}", f"LLM request failed: {str(e)}")

def annotate_notebook(nb: NotebookNode) -> NotebookNode:
    print("✏️  Annotating notebook with markdown comments...")
    new_cells = []
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == "code":
            markdown_comment = infer_commentary(cell.source, i)
            new_cells.append(new_markdown_cell(markdown_comment))
            new_cells.append(cell)
        else:
            new_cells.append(cell)
    print("✅ Annotation complete.")
    nb.cells = new_cells
    return nb

def save_notebook(nb: NotebookNode, output_path: str):
    print(f"💾 Saving annotated notebook to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        write(nb, f)
    print("✅ Notebook saved successfully.")

def process_notebook(input_path: str, output_path: str):
    nb = read_notebook(input_path)
    annotated_nb = annotate_notebook(nb)
    save_notebook(annotated_nb, output_path)
    print("🚀 Opening the output notebook...")
    os.system(f"jupyter notebook {output_path}")

# Example usage:
process_notebook("input.ipynb", "output_commented.ipynb")
