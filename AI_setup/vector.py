from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd 

csv_path = os.path.join(os.path.dirname(__file__), "pizza_reviews.csv")
df = pd.read_csv(csv_path)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " "+ row["Review"],
            metadata={"Rating":row["Rating"], "date": row["Date"]}
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="pizza_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents: 
    vector_store.add_documents(documents=documents, ids=ids)

#return the top 3 most similar documents from the vector store
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":3})