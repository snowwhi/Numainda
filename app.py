import os
import gradio as gr
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

print("⏳ Loading vector database...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
vectordb = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
print("✅ Vector database loaded!")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
llm = ChatGroq(
    api_key=GROQ_API_KEY,
)


Context:
{context}

Question:
{question}

Answer:


)

def answer_question(question, history):
    if not question.strip():
        return "", history
    try:
        seen = set()
        sources = []
            src = doc.metadata.get("source_file", "Unknown")
            page = doc.metadata.get("page", "?")
            entry = f"📄 {src} — Page {page}"
            if entry not in seen:
                seen.add(entry)
                sources.append(entry)
        full_answer = answer + sources_text
    except Exception as e:

    return "", history

    )

    chatbot = gr.Chatbot(
    )

    with gr.Row():
        msg = gr.Textbox(
        )


    gr.Examples(
        examples=[
            "What did MNAs say about inflation?",
        ],
    )

    submit_btn.click(answer_question, [msg, chatbot], [msg, chatbot])
    msg.submit(answer_question, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot)

demo.launch()