# Usage
# markdown-chat init-knowledge-base
# markdown-chat chat

from openai_client import generate_embeddings


def main():
    text = "This is a sample text"
    embeddings = generate_embeddings(text)
    print(embeddings)

def init_knowledge_base():
    # files = get_files()
    # embeddings = get_embeddings(files)
    # db = init_db()
    # db.populate_db(file, embeddings)
    pass

def chat():
    # db = load_db()
    # while True:
    #     query = input("...")
    #     query_embedding = get_embeding(query)
    #     chunks = get_related_chunks(query_embedding)
    #     print(ask_llm(query, chunks))
    pass

if __name__ == "__main__":
    main()
