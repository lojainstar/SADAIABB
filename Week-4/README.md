# Arabic RAG Chatbot

This project is an Arabic Retrieval-Augmented Generation (RAG) chatbot built using modern NLP and Information Retrieval techniques.
The system retrieves relevant Arabic text chunks from a dataset and uses a Large Language Model (LLM) to generate accurate responses.

---

## Project Overview

The project was developed to demonstrate the complete RAG pipeline for Arabic language applications, including:

* Arabic dataset processing
* Text chunking
* Embedding generation
* Vector database indexing
* Retrieval systems
* LLM-based response generation
* Interactive chatbot interface

---

## Dataset

We used the Arabic dataset:

[Arabic Wikipedia Sentences Dataset](https://huggingface.co/datasets/deokhk/ar_wiki_sentences_1000000?utm_source=chatgpt.com)

### Dataset Features

* Arabic textual content
* More than 30,000 samples
* Suitable for Retrieval-Augmented Generation systems
* Clean and structured sentences

---

## Chunking Methods

The dataset was divided into chunks using multiple splitting techniques:

### 1. Fixed Chunking

Implemented using:

* `CharacterTextSplitter`

### 2. Recursive Chunking

Implemented using:

* `RecursiveCharacterTextSplitter`

### 3. Semantic Chunking

Implemented using:

* Sentence embeddings
* Cosine similarity

These methods help improve retrieval quality and context understanding.

---

## Embedding Model

We used the multilingual embedding model:

[intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base?utm_source=chatgpt.com)

### Why This Model?

* Supports Arabic language
* Strong semantic understanding
* Suitable for vector similarity search
* Works efficiently with FAISS

---

## Vector Database

The project uses:

[FAISS](https://github.com/facebookresearch/faiss?utm_source=chatgpt.com)

FAISS was used to:

* Store embedding vectors
* Perform similarity search
* Retrieve the most relevant text chunks

---

## Retrieval Methods

### FAISS Retriever

Semantic retrieval based on vector similarity.

### BM25 Retriever

Implemented using:

[LangChain Community](https://python.langchain.com/?utm_source=chatgpt.com)

BM25 provides keyword-based retrieval for Arabic documents.

---

## Large Language Model (LLM)

The chatbot uses:

[GroqCloud](https://console.groq.com/?utm_source=chatgpt.com)

with the model:

```python
llama-3.1-8b-instant
```

### Purpose of the LLM

* Generate final answers
* Use retrieved context
* Reduce hallucinations
* Improve response accuracy

---

## RAG Pipeline

The chatbot workflow:

```text
User Question
↓
Embedding Generation
↓
FAISS / BM25 Retrieval
↓
Relevant Chunk Retrieval
↓
LLM Prompt Construction
↓
Final Response Generation
```

---

## Technologies Used

* Python
* Hugging Face Datasets
* Sentence Transformers
* FAISS
* LangChain
* BM25 Retriever
* Groq API
* Gradio

---

## User Interface

The chatbot interface was built using:

[Gradio](https://www.gradio.app/?utm_source=chatgpt.com)

This allows users to interact with the Arabic RAG chatbot through a simple web interface.

---

## Objective

The main objective of this project is to build a complete Arabic RAG system capable of:

* Understanding Arabic queries
* Retrieving relevant Arabic information
* Generating context-aware responses
* Demonstrating modern NLP and Retrieval techniques

---

## Authors

Developed as an educational NLP and RAG project using Arabic datasets and modern Large Language Models.

