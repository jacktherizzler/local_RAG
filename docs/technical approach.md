# technical approach rag faq chatbot

## implementation approach
the rag pipeline uses n8n to build a local faq chatbot
input user questions via a chat webhook
document processing pdfs are extracted split into chunks and enriched with contextual summaries using ollama
embeddings ollama nomic embed text model generates dense vectors
sparse vectors tf idf vectors are created using python code
vector store qdrant stores dense and sparse vectors for retrieval
llm ollama llama3.1 8b generates responses with retrieved context
memory langchain window buffer keeps 10 prior interactions
retrieval uses bm25 reranking for better results

## rationale
local setup ollama and qdrant avoid api costs and ensure privacy
n8n chosen for modular workflow and langchain integration
qdrant supports sparse and dense vectors for advanced retrieval
ollama models nomic embed text for embeddings and llama3.1 8b for generation balance performance and resources
contextual summaries improve retrieval accuracy
bm25 reranking enhances result relevance

## challenges and solutions
challenge no external api access
solution used ollama for embeddings and generation qdrant for vector storage
challenge sparse vector support in langchain
solution used qdrant client directly with custom code
challenge local llm performance
solution optimized chunk sizes used lightweight models
challenge conversation continuity
solution added langchain window buffer memory

## workflow design decisions
chat trigger simplifies input via webhook
modular nodes separate steps for clarity
contextual summaries generated before vectorization
sparse and dense vectors combined for hybrid retrieval
reranking improves result quality
error handling n8n retry mechanism used

## performance considerations
latency sparse vector retrieval and caching reduce response time
memory qdrant persists vectors to disk
scalability limited by local hardware can improve with quantized models

## ideas for scalability and improvements
real time indexing add file watcher for new documents
multi modal support use ocr for images or tables
analytics log queries to sqlite for insights
multiple llms support model switching in n8n
webhook integrations add slack or discord endpoints


