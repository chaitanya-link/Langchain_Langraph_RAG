"""
Phase 1 - RAG basics: chunking, embedding, retrieval
Runs offline using TF-IDF as a stand-in for a real embedding model.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: "documents" - in real RAG these come from a PDF/website loader
raw_text = """
Python is a high-level programming language known for readability.
LangChain is a framework for building applications powered by LLMs.
Vector databases store embeddings and support similarity search.
RAG combines retrieval with generation to ground LLM answers in real data.
FastAPI is a Python web framework used to build fast APIs.
"""

# STEP 2: CHUNKING - one sentence = one chunk, kept simple for learning
chunks = [c.strip() for c in raw_text.strip().split("\n") if c.strip()]

# STEP 3: EMBEDDING - TF-IDF stands in for GoogleGenerativeAIEmbeddings later
vectorizer = TfidfVectorizer()
chunk_vectors = vectorizer.fit_transform(chunks)  # this is the "vector DB" build step

# STEP 4: RETRIEVAL
def retrieve(question, top_k=2):
    question_vector = vectorizer.transform([question])             # embed the query
    scores = cosine_similarity(question_vector, chunk_vectors)[0]   # compare to every chunk
    ranked = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]

# STEP 5: "GENERATION" - stubbed here; real RAG sends this to an LLM
def answer(question):
    top_chunks = retrieve(question)
    print(f"\nQuestion: {question}")
    for chunk, score in top_chunks:
        print(f"  [{score:.3f}] {chunk}")
    print("-> This context would now be sent to an LLM with the question.")


if __name__ == "__main__":
    answer("what is used to build web APIs in python")
    answer("how does semantic search work")