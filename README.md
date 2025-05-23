# 📘 Ipynb Auto Commenter

Automatically annotate Jupyter Notebooks (`.ipynb`) by inserting intelligently generated markdown comments before each code cell. This project now includes a **FastAPI-based web interface** with file upload support and auto-download functionality.

---

## 🚀 Features

- Parses `.ipynb` notebooks
- Sends each code block to a local LLM (via [Ollama](https://ollama.com/))
- Generates markdown comments in the format:

  ```markdown
  # Title

  ## Subtitle

  Explanation
  ```

- Prepends comments above each code cell
- Exposes this functionality through a user-friendly web interface
- Auto-deletes temporary files after serving response

---

## 🧠 What It Looks Like

You upload a Jupyter Notebook → It returns a downloadable `.ipynb` file with comments added above each cell.

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ipynb-auto-commenter.git
cd ipynb-auto-commenter
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Install Ollama and run a local model like `llama3`:

```bash
ollama run llama3
```

Make sure Ollama is running on `http://localhost:11434`.

---

## 🚀 Run the FastAPI App

From the root directory:

```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🖥️ Web Interface

- Upload any `.ipynb` file
- The backend processes the notebook and returns a modified notebook
- The file is automatically downloaded and temporary files are deleted

---

## 📦 Directory Structure

```
.
├── auto_comment.py          # Core logic for commenting notebooks
├── app/
│   ├── main.py              # FastAPI app
│   ├── templates/
│   │   └── index.html       # Upload form
│   └── static/
│       └── style.css        # Basic styling
├── requirements.txt
├── README.md
```

---

## 🧠 Learning Highlights

This project demonstrates:

- File upload/download in FastAPI
- Using `BackgroundTasks` for cleanup
- HTML/CSS frontend with Jinja2 templates
- Integration with local LLM via Ollama
- Dynamic notebook manipulation with `nbformat`

---

## 📋 Requirements

- Python 3.8+
- `fastapi`, `uvicorn`, `jinja2`, `nbformat`, `requests`, `python-multipart`
- Ollama (local LLM runner)

---

## 📄 License

MIT License. Free to use, modify, and extend.

---

## 🙌 Acknowledgements

Built with ❤️ using Python, FastAPI, and Ollama.
