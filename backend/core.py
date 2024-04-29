import os
from typing import Any

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PineconeLangChain

load_dotenv()
pc = Pinecone(
    api_key=os.environ.get('PINECONE_API_KEY')
)


def run_llm(query: str) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = PineconeLangChain.from_existing_index(index_name='langchain-doc-index',
                                                      embedding=embeddings)

    chat = ChatOpenAI(verbose=True, temperature=0)

    qa = RetrievalQA.from_chain_type(llm=chat,
                                     chain_type='stuff',
                                     retriever=docsearch.as_retriever(),
                                     return_source_documents=True,)

    return qa({'query': query})


if __name__ == '__main__':
    print(run_llm(query='What are dunder methods ?'))