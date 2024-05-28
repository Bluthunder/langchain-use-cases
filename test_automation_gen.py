import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_pinecone import Pinecone, PineconeVectorStore

from tools.utils import clean_response, write_to_file
from tools.document_loader import github_files_loader, document_splitter
from tools.vector_embeddings import insert_into_pinecone, retrieval_qa


def llm_initialize():
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    return llm


def generate_feature_file(user_story_text: str) -> str:
    scenario_template = '''
    Given the user story {user_story} about a feature, i want to create all possible scenarios in BDD feature file format using cucumber
    '''
    scenario_prompt_template = PromptTemplate(
        input_variables=['user_story'],
        template=scenario_template
    )

    chain = LLMChain(llm=llm_initialize(),
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

    chain = LLMChain(llm=llm_initialize(), prompt=test_gen_prompt_template)
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

    chain = LLMChain(llm=llm_initialize(), prompt=page_obj_gen_prompt_template)

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

    # Page Object Generation

    # RAG
    rag_prompt = """
    You are javascript test automation developer. Reply with complete code for page object classes
    {question}.
    Please follow the below guidelines 
    1. Use context to understand code and create similar page objects.
    2. Write complete code with implementations according to the question
    3. In case of external dependencies use proper import statements
    
    Question:
    {question}
    
    Context:
    {context}
    
    """

    rag_prompt_template = PromptTemplate(template=rag_prompt,
                                         input_variables=["context", "question"])

    embeddings = OpenAIEmbeddings()
    index_name = os.environ.get('INDEX_NAME')

    docsearch = Pinecone.from_existing_index(index_name=index_name,
                                             embedding=embeddings)

    qa_chain = RetrievalQA.from_llm(llm=llm_initialize(),
                                    prompt=rag_prompt_template,
                                    retriever=docsearch.as_retriever(),
                                    return_source_documents=True)

    results = qa_chain({"query": page_obj})

    print(results)
