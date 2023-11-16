# Usage
# markdown-chat init-knowledge-base
# markdown-chat chat

def main():
    pass


def init_knowledge_base():
    files = get_files()
    embeddings = get_embeddings(files)
    db = init_db()
    db.populate_db(file, embeddings)


def chat():
    db = load_db()
    while True:
        query = input("...")
        query_embedding = get_embeding(query)
        chunks = get_related_chunks(query_embedding)
        print(ask_llm(query, chunks))


if __name__ == "__main__":
    main()
