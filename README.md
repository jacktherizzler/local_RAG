# local_RAG

## overview
this project builds a retrieval augmented generation faq chatbot using n8n ollama and qdrant all running locally. it processes pdf or text documents uses sparse and dense vectors for retrieval keeps conversation history and supports contextual summaries for better search.

## prerequisites
you need these tools installed
docker for n8n redis and qdrant
python 3.9 or higher
ollama with nomic embed text and llama3.1 8b models
node.js for n8n dependencies
git for cloning the repository

## setup instructions
follow these steps to set up the project locally

1 clone repository
run these commands
git clone <repository url>
cd rag chatbot project

2 install python dependencies
run this command
pip install r requirements.txt

3 set up n8n locally
run this command to start n8n in docker
docker run d name n8n p 5678:5678 v ~/.n8n:/home/node/.n8n n8nio/n8n

4 set up redis locally
run this command to start redis in docker
docker run d name redis p 6379:6379 redis

5 set up qdrant locally
run this command to start qdrant in docker
docker run d name qdrant p 6333:6333 qdrant/qdrant

6 set up ollama locally
download and install ollama from ollama.com
run these commands to start ollama and pull models
ollama serve
ollama pull nomic embed text
ollama pull llama3.1:8b

7 setup qdrant collection
run this command to create the qdrant collection
python scripts/setup.py

8 import n8n workflow
open n8n at http://localhost:5678
import workflows/local_RAG.json
configure ollama credentials with base url http://localhost:11434
configure redis credentials with host localhost and port 6379

9 place documents
add faq pdfs to data/sample documents/

10 test workflow
send a post request to http://localhost:5678/webhook/<webhook id> with json
{
  "message": "what is altibbe health mission"
}
or use the sample html form in scripts/form.html

## environment variables
set these variables in your environment
n8n host: localhost
ollama host: http://localhost:11434
redis host: localhost
redis port: 6379
qdrant host: http://localhost:6333

## testing
sample queries are in tests/sample queries.json
run tests with this command
curl x post http://localhost:5678/webhook/<webhook id> d '{"message": "what is altibbe health"}' h "content type: application/json"

## project structure
rag chatbot project/
workflows/
  local_RAG.json
scripts/
  setup.py
  form.html
docs/
  readme.md
  technical approach.md
data/
  sample documents/
tests/
  sample queries.json


