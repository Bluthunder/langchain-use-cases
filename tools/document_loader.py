import os

from pprint import pprint
from langchain_community.document_loaders import GithubFileLoader
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()
ACCESS_TOKEN = os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN')


def github_files_loader(repo_name: str, branch_name: str, directory: str) -> object:
    loader = GithubFileLoader(
        repo=repo_name,
        access_token=ACCESS_TOKEN,
        github_api_url="https://api.github.com",
        branch=branch_name,
        file_filter=lambda file_path: file_path.startswith(directory)

    )
    documents = loader.load()

    return documents


def document_splitter(chunk_size: int, chunk_overlap: int, documents: list) -> list:
    text_spliter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_spliter.split_documents(documents)

    return texts
