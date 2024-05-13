from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA


def insert_into_pinecone(texts: list, embeddings: object, index_name: str) -> object:
    doc = PineconeVectorStore.from_documents(text=texts,
                                             embedding=embeddings,
                                             index_name=index_name)

    return doc


def retrieval_qa(doc: object, llm: object) -> object:
    qa = RetrievalQA.from_chain_type(llm=llm,
                                     chain_type="stuff",
                                     retriever=doc)

    return qa
