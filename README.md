# 🧠 RAG Pipeline for PDFs — modular & containerized

This project implements a reproducible, Docker-ready Retrieval-Augmented Generation (RAG) pipeline using LangChain, PyPDFLoader, OpenAI embeddings, GPT-4, and Chroma vectorstore. It supports modular architecture, and context-aware prompting for (hopeful) minimal hallucinations.

---

## 📂 Project Structure

```
rag_project/
├── data/			    # Drop zone for PDFs
├── chroma_db/ 			# Persistent vectorstore
├── config.py 			# API key and chunking variables
├── loaders.py 			# PDF loading logic
├── splitter.py 		# Chunking strategy
├── embeddings.py 		# Embedding setup
├── vectorstore.py 		# Chroma setup
├── retriever.py 		# Retriever configuration
├── prompt.py 			# Prompt templates
├── rag_chain.py 		# Chain assembly
├── query.py 			# Interactive query logic
└── main.py 			# Entry point
```


## 🚀 Quickstart

1. **Create and activate a virtual environment**  
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows  
    ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your OpenAI key**  
    Create a `.env` file within the file directory with:
    
    ```env
    OPENAI_TOKEN=your-api-key-here
    ```
    
4. **Create a folder `data` within the file directory and drop PDFs there**  
The folder `chroma_db` is automatically created.


5. **Run the pipeline**
    
    ```bash
    python main.py
    ```
    

----------

## 🧩 Features

-   ✅ Token-based chunking with overlap
-   ✅ MMR retrieval (provided best results among different setups)
-   ✅ Context-bound prompting with fallback logic
-   ✅ Modular components for easy testing and extension
-   ✅ Full Docker support for isolated environments and secure `.env` injection

----------

## 🛠️ Configuration

Edit `config.py` to adjust:

-   API keys
-   Chunk size / overlap  
-   Directory for PDF storage
-   Directory for a Chroma database

----------

## 📚 Prompt Template

```text
You are a concise assistant who answers questions strictly based on the provided context.
Use only the information from the context to answer the question.
If the answer is not clearly stated in the context, say so honestly.
Question: {input}
Context: {context}
Answer:
```

----------

## 🧪 Testing

To run a default query:

```bash
python main.py
```

If no input is provided, a test query is created:

```text
Who is named in the text? Include no meta data!
```
----------

## 🐳 Docker Support


### 📦 Build the Docker Image

```bash
docker build -t rag-pipeline .
```

-   `rag-pipeline` is the image name — change it if needed.
-   The build uses `python:3.11-slim` and creates a virtual environment inside the container.

----------

### 🚀 Run the Container
in **Windows PowerShell**:
```Windows PowerShell
docker run -it --env-file "C:\path\to\.env" `
   -v "C:\path\to\data:/data" `
   rag-pipeline
```

-  Update `C:\path\to\` to match the location of your files.
- `-it` is required to run the container interactively
- `--env-file .env` injects your API keys.
-   `-v "C:\path\to\data:/data"` mounts `data` with PDFs into the container.



----------

### 📁 Recommended `.dockerignore`

```dockerignore
# Python artifacts
__pycache__/
*.pyc
*.pyo
*.pyd

# Secrets and local data
.env
data/
chroma_db/

# Git
.git/
.gitignore
```

This keeps your image clean and secure by excluding local caches, data, and version history.

----------

## ⚠️ Note  
The system was tested with one page PDF files containing plain text. Technically, PyPDFLoader should be able to handle PDF files with multiple pages, too.

For more structured PDF files (with layout elements such as tables, columns, headers, sections, etc.) more advanced layout-aware models, which understand both the text and its spatial arrangement on the page, might be more beneficial.

----------

## 📖 License

This project is licensed under MIT License. See `LICENSE.md`  
You are free to use, modify, and distribute this code for personal or commercial purposes, provided that the original copyright and license notice are retained.
