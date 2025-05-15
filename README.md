# Ipynb Auto Commenter

Automatically annotate Jupyter Notebooks (`.ipynb`) by inserting intelligently generated markdown comments before each code cell. This tool uses [Ollama](https://ollama.com/) to call a local LLM (like `llama3`) and produce readable, structured documentation in the format:

```markdown
# Title

## Sub title

Explanation
```

---

## Features

- Reads `.ipynb` notebooks and analyzes code cells
- Uses a local LLM (via Ollama) to infer purpose of each code block
- Adds a markdown explanation before each code block
- Saves and opens the modified notebook automatically

---

## Example Output Format

Each code cell will be preceded by a markdown cell like:

```markdown
# Data Loading

## Reading data using pandas

This code loads the dataset from a CSV file using pandas.
```

```python
df = pd.read_csv("my_data.csv")
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ipynb-auto-commenter.git
cd ipynb-auto-commenter
```

### 2. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install and run Ollama

Install [Ollama](https://ollama.com/) and run a model:

```bash
ollama run llama3
```

Make sure Ollama is accessible at `http://localhost:11434`.

---

## Usage

### 1. Add a Jupyter Notebook (e.g., `input.ipynb`) to the project root.

### 2. Modify `main.py` or use directly:

```python
from main import process_notebook
process_notebook("input.ipynb", "output_commented.ipynb")
```

### 3. Or run from terminal (if enabled as CLI):

```bash
python main.py
```

---

## Output

A new `.ipynb` file (e.g., `output_commented.ipynb`) will be created with comments auto-inserted and opened in your Jupyter environment.

---

## Requirements

- Python 3.8+
- `nbformat`
- `requests`
- Ollama with a local LLM (e.g., llama3)

---

## Future Work

- Support for cloud-hosted LLMs
- Topic grouping and section headers
- Custom prompt templates
- GUI inclusion

---

## License

MIT License. Free to use and modify.

---

## Acknowledgements

Built with using Python, Jupyter, and Ollama.
