from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__ == '__main__':
    load_dotenv()
    print("Hello Langchain")
    problem = '''
    Breadth First Search
    '''
    summary_template = '''
    Given the problem {problem} about a coding challenge I want you to create:
     Actual Implementation using python 3
    '''

    summary_prompt_template = PromptTemplate(input_variables=['problem'], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"problem": problem})
    print(res)

    with open("result/codegen.py", "w") as code_file:
        code_file.write("# This is AI generated file !!!!")
        for line in res:
            code_file.write(line + '\n')
            # Optionally, print the data as it is written to the file
            print(line)
            # code_file.writelines(res)


