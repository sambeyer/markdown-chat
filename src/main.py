# Usage
# markdown-chat init-knowledge-base
# markdown-chat chat
from db import insert_embedding, setup_database
from openai_client import generate_embeddings
import os

DB_NAME = "memory.db"


def main():
    init_knowledge_base()


def get_markdown_files(folder_path):
    """
    Retrieve all markdown files from the specified folder.
    """
    markdown_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            markdown_files.append(os.path.join(folder_path, filename))
    return markdown_files


def init_knowledge_base():
    folder_path = "./files"  # Adjust the path as necessary
    markdown_files = get_markdown_files(folder_path)

    setup_database(DB_NAME)

    for file_path in markdown_files:
        # Read the file content
        with open(file_path, "r") as file:
            content = file.read()
            embeddings = generate_embeddings(content)
            insert_embedding(DB_NAME, file_path, content, embeddings)
            print(f"Generated embeddings for {file_path}")


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
