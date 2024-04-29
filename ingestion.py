import os

from dotenv import load_dotenv
from langchain_community.document_loaders import ReadTheDocsLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeLangchain
from pinecone import Pinecone

load_dotenv()
pc = Pinecone(
    api_key=os.environ.get('PINECONE_API_KEY')
)
def ingest_doc_from_readdocsloader():
    loader = ReadTheDocsLoader(path='documents/langchain.readthedocs.io/en/latest', encoding='ISO-8859-1')
    raw_documents = loader.load()
    text_splitters = RecursiveCharacterTextSplitter(chunk_size=5000,
                                                    chunk_overlap=200,
                                                    separators=['\n\n', '\n', " ", ""])
    documents = text_splitters.split_documents(documents=raw_documents)
    print(f'Splitting into {len(documents)} chunks')

    for docs in documents:
        old_path = docs.metadata["source"]
        new_url = old_path.replace('langchain-docs', 'https:/')
        docs.metadata.update({'source': new_url})

    embeddings = OpenAIEmbeddings()
    PineconeLangchain.from_documents(documents, embeddings, index_name='langchain-doc-index')


def ingest_doc_pdf():
    loader_ = PyPDFLoader('C:\\Users\\KAUSHIK\\Downloads\\ObjectOrientedPython.pdf')
    pdf_doc = loader_.load()
    text_splitters_ = CharacterTextSplitter(chunk_size=100,
                                               chunk_overlap=20,
                                               separator='\n')

    documents_ = text_splitters_.split_documents(documents=pdf_doc)
    print(f'Splitting into {len(documents_)} chunks')

    embeddings_ = OpenAIEmbeddings()
    PineconeLangchain.from_documents(documents_, embeddings_, index_name='langchain-doc-index')




if __name__ == '__main__':
    # ingest_doc_from_readdocsloader()
    ingest_doc_pdf()


