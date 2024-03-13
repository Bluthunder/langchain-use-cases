from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor

from tools.tools import get_profile_url

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    template = """ Given the full name {name_of_person} I want you to get me a link to their  linkedin profile page
                     Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=['name_of_person']
    )

    tools_for_agent = [
            Tool(
                name="Crawl google for linkedin profile page",
                func=get_profile_url,
                description="useful for when you need get the linkedin page url")
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )
    result = agent_executor.invoke(
        input={'input': prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result['output']

    return linkedin_profile_url
