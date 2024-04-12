from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from tools.utils import clean_response, write_to_file
import re


def generate_feature_file(user_story_text: str) -> str:
    scenario_template = '''
    Given the user story {user_story} about a feature, i want to create all possible scenarios in BDD feature file format using cucumber
    '''
    scenario_prompt_template = PromptTemplate(
        input_variables=['user_story'],
        template=scenario_template
    )
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = LLMChain(llm=llm,
                     prompt=scenario_prompt_template)

    res = chain.run(user_story=user_story_text)

    return res


def generate_step_def(features: str) -> str:
    test_gen_template = '''
    Given a .feature file{feature} generate test automation step definition with code in js for 
    selenium page object model
    '''
    test_gen_prompt_template = PromptTemplate(
        input_variables=['feature'],
        template=test_gen_template
    )

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    chain = LLMChain(llm=llm, prompt=test_gen_prompt_template)
    res = chain.run(feature=features)

    return res


def generate_page_object(step_def: str) -> str:
    page_obj_gen_template = """
    Given step def file {step_defs} generate a page object class with all interaction methods implemented
    """
    page_obj_gen_prompt_template = PromptTemplate(
        input_variables=['step_def'],
        template=page_obj_gen_template
    )
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = LLMChain(llm=llm, prompt=page_obj_gen_prompt_template)

    res = chain.run(step_defs=step_def)

    return res


if __name__ == '__main__':
    load_dotenv()
    print("Hello Test Generation")

    feature = generate_feature_file('OTT Playback Scenario')
    # print(feature)
    write_to_file('features/Playback', 'feature', feature)

    step_def = generate_step_def(feature)
    # print(step_def)
    step_def = clean_response(step_def)
    write_to_file('step_defs/Playback', 'js', step_def)

    page_obj = generate_page_object(step_def)
    # print(page_obj)
    page_obj = clean_response(page_obj)
    write_to_file('page_objects/Playback', 'js', page_obj)
