# 🏛️ Numainda — نُمائندہ
### An AI-Powered Search Engine for Pakistan's National Assembly Records
## 📌 What is Numainda?

**Numainda** (Urdu: نُمائندہ — meaning *"Representative"*) is an AI-powered question-answering system built on top of Pakistan's National Assembly parliamentary records. It allows journalists, students, researchers, activists, and ordinary citizens to search through 50+ years of parliamentary history using plain English or Urdu questions — and get clear, sourced answers in seconds.

> *"Imagine Google, but it only reads Pakistan's parliament records. You ask a question about what politicians said, and it gives you the exact answer with a link to the original speech."*

---

## 🔍 The Problem

Pakistan's National Assembly has been publishing official records of every debate, speech, question, and bill since 1973. These records are publicly available — but entirely inaccessible in practice.

- They exist as **thousands of unstructured PDFs**
- There is **no search functionality** on the official website
- Journalists spend **hours manually reading documents** to fact-check a single claim
- Citizens have **no practical way** to hold their representatives accountable
- Researchers spend **days or weeks** tracing legislative history

**Numainda fixes this.**

---

## ✅ The Solution

Type a question. Get an answer. With proof.

| You Ask | Numainda Does | You Get |
|---------|--------------|---------|
| *"What did MNAs say about inflation?"* | Searches 18,897 chunks of parliamentary text | A clear, human answer with source documents cited |
| *"Which questions were raised about education?"* | Retrieves the most relevant speeches and debates | A summary of key points with PDF references |
| *"What was discussed about electricity prices?"* | Finds exact sessions where this was debated | Named speakers, dates, and document links |

---

## 🗂️ Dataset

- **Source:** Official Pakistan National Assembly website (na.gov.pk)
- **Format:** PDF documents (parliamentary proceedings, debates, question hours)
- **Volume:** 360+ PDFs covering recent National Assembly sessions
- **Processing:**
  - Text extracted using PyPDF
  - Cleaned to remove headers, footers, page numbers, and noise
  - Split into 18,897 searchable chunks
  - Embedded using multilingual sentence transformers
  - Stored in a FAISS vector database

---

## ⚙️ How It Works

```
User Question
      ↓
Convert to Vector Embedding
      ↓
Search FAISS Vector Database
      ↓
Retrieve Top 5 Most Relevant Chunks
      ↓
Feed Chunks + Question to LLM (Groq)
      ↓
Generate Human Answer with Sources
      ↓
Display to User with Document References
```

This architecture is called **RAG — Retrieval Augmented Generation**. It grounds the AI's answers in real documents rather than hallucinated knowledge.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **PDF Processing** | PyPDF, LangChain Document Loaders |
| **Text Chunking** | LangChain RecursiveCharacterTextSplitter |
| **Embeddings** | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` |
| **Vector Database** | FAISS (Facebook AI Similarity Search) |
| **LLM** | Llama 3.3 70B via Groq API |
| **Orchestration** | LangChain Core (LCEL) |
| **UI** | Gradio |
| **Hosting** | Hugging Face Spaces |
| **Language** | Python 3.10+ |

---

## 🚀 Live Demo

Try it here → **[huggingface.co/spaces/khadijahanif/Hackathon](https://huggingface.co/spaces/khadijahanif/Hackathon)**

---

## 📁 Project Structure

```
numainda/
│
├── app.py                  # Main Gradio application
├── build_index.py          # Script to build FAISS index from PDFs
├── requirements.txt        # Python dependencies
│
├── faiss_index/
│   ├── index.faiss         # Vector database (binary)
│   └── index.pkl           # Metadata store
│
└── README.md               # This file

## 💡 Example Questions to Try

- *"What did MNAs say about inflation in recent sessions?"*
- *"Which questions were raised about education funding?"*
- *"What was debated about electricity prices?"*
- *"What promises were made about unemployment?"*
- *"Who spoke about healthcare and what did they say?"*
- *"What bills were introduced in April 2025?"*

---

## 🎯 Impact

| Who Benefits | How |
|-------------|-----|
| **Journalists** | Fact-check politician claims in seconds instead of hours |
| **Students** | Research Pakistani legislative history in minutes |
| **Activists** | Track promises made vs promises kept |
| **Researchers** | Analyze voting patterns and debate trends |
| **Citizens** | See exactly what their MNA said and did |

---

## 👥 Team

Built with ❤️ for the HSE iCode / Guru / Park Angels Hackathon

| Name | Role |
|------|------|
| **Ayesha Bint Abdullah** | Team Lead |
| **Khadija Hanif** | Developer |
| **Ahmed Abdullah** | Developer |
| **Abdul Qadir Khan** | Developer |
| **Ahmad Hassan** | Developer |

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Pakistan National Assembly](https://na.gov.pk) for publishing open parliamentary records
- [Groq](https://groq.com) for free, blazing-fast LLM inference
- [Hugging Face](https://huggingface.co) for free model hosting and Spaces
- [LangChain](https://langchain.com) for the RAG framework
- [FAISS](https://github.com/facebookresearch/faiss) by Meta AI for vector search

---

> *"We are not just building a chatbot. We are building accountability."*
