from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_party.linkedin import scrape_linkedin_profile, mock_linkedin_request

if __name__ == '__main__':
    load_dotenv()
    print("Hello Langchain")

    linkedin_profile_url = linkedin_lookup_agent(name='Satya Nadella')
    summary_template = '''
    Given the information {information} about a person I want you to create:
    1. A short Summary
    2. Two interesting facts about them
    '''
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    """
    This is for making request to linkedin using proxyCurl
    """
   # linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/kaushiktd/')
    # print(linkedin_data)

    """
    This is mocked response from gist github
    """

    # mocked_data = mock_linkedin_request()
    # print(mocked_data.json())

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    res = chain.run(information=linkedin_data)

    print(res)
