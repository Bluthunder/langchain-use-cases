import os

from langchain_community.document_loaders import GithubFileLoader
from dotenv import load_dotenv

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


if __name__ == '__main__':
    github_documents = github_files_loader("bluthunder/webdriverio-mocha-docker",
                                           "master-new",
                                           "test/pageobjects")

    print(github_documents)