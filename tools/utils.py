import re

from langchain_openai import ChatOpenAI


def clean_response(response: str) -> str:

    if "```javascript```" in response:
        print("trimming all the comments")
        response = re.search(r'`javascript(.+?)`', response, re.DOTALL).group(1).strip()
        print("Clean Response ---> ", response)
    else:
        response = response
    return response


def write_to_file(file_name: str, file_ext: str, input: str) -> None:
    with open(file_name + '.' + file_ext, 'w') as file:
        file.write("# File \n")
        file.write(input)



def getModel(temp: int, model_name: str) -> object:
    llm = ChatOpenAI(temperature=temp,
                     model_name=model_name)
    return llm