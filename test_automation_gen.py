from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


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


def generate_automation_code(features: str) -> str:
    test_gen_template = '''
    Given a .feature file{feature} generate test automation step definition with code written in js for 
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


def write_to_file(file_name: str, file_ext: str, input: str) -> None:
    with open(file_name + '.' + file_ext, 'w') as file:
        file.write("# Feature File \n")
        file.write(input)


if __name__ == '__main__':
    load_dotenv()
    print("Hello Test Generation")

    feature = generate_feature_file('OTT Playback Scenario')
    print(feature)

    write_to_file('features/Playback', 'feature', feature)

    step_def = generate_automation_code(feature)
    write_to_file('step_defs/Playback', 'js', step_def)
