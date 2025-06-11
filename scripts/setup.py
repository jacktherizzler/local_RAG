import qdrant_client
from qdrant_client.http.models import Distance, VectorParams

def setup_qdrant():
    client = qdrant_client.QdrantClient(host="localhost", port=6333)
    try:
        client.create_collection(
            collection_name="contextual_retrieval_example",
            vectors_config={
                "default": VectorParams(size=768, distance=Distance.COSINE)
            },
            sparse_vectors_config={
                "bm42": {"modifier": "idf"}
            }
        )
        print("qdrant collection contextual_retrieval_example created")
    except Exception as e:
        print(f"error setting up qdrant: {e}")

if __name__ == "__main__":
    setup_qdrant()
