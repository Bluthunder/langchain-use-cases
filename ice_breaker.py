from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel
from third_party.linkedin import scrape_linkedin_profile, mock_linkedin_request


def ice_breaker(name: str) -> tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    summary_template = '''
       Given the information {information} about a person I want you to create:
       1. A short Summary
       2. Two interesting facts about them
       3. Creative Ice Breaker to Open Conversation with them
       \n{format_instructions}
       '''
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    """
    This is mocked response from gist github
        # mocked_data = mock_linkedin_request()
        # print(mocked_data.json())
    """

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.run(information=linkedin_data)
    print(res)

    return person_intel_parser.parse(res), linkedin_data.get('profile_pic_url')


if __name__ == '__main__':
    load_dotenv()
    print("Hello Langchain !!!, I will be processing linkedin Data")

    result = ice_breaker(name='arijit-das-5039a237')
