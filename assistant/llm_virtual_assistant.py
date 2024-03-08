import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

url = "https://us-south.ml.cloud.ibm.com"

watsonx_project_id = ""
api_key = ""

def get_credentials():
    load_dotenv()
    globals()["api_key"] = os.getenv("api_key", None)
    globals()["watsonx_project_id"] = os.getenv("project_id", None)

def get_model(model_type, max_tokens, min_tokens, decoding, temperature):
    generate_params = {
        GenParams.MAX_NEW_TOKENS: max_tokens,
        GenParams.MIN_NEW_TOKENS: min_tokens,
        GenParams.DECODING_METHOD: decoding,
        GenParams.TEMPERATURE: temperature
    }

    model = Model(
        model_id=model_type,
        params=generate_params,
        credentials={
            "apikey": api_key,
            "url": url
        },
        project_id=watsonx_project_id
    )

    return model

def get_lang_chain_model(model_type, max_tokens, min_tokens, decoding, temperature):
    base_model = get_model(model_type, max_tokens, min_tokens, decoding, temperature)
    langchain_model = WatsonxLLM(model=base_model)

    return langchain_model

def main():
    get_credentials()
    question = "What are the limitations of generative AI models?"
    file_path = "./Generative_AI_Overview.pdf"

    answer_questions_from_doc(api_key, watsonx_project_id, file_path, question)

def answer_questions_from_doc(request_api_key, request_project_id, file_path, question):
    globals()["api_key"] = request_api_key
    globals()["watsonx_project_id"] = request_project_id

    model_type = "meta-llama/llama-2-70b-chat"
    max_tokens = 300
    min_tokens = 100
    decoding = DecodingMethods.GREEDY
    temperature = 0.7

    model = get_lang_chain_model(model_type, max_tokens, min_tokens, decoding, temperature)

    loaders = [PyPDFLoader(file_path)]

    index = VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)).from_loaders(loaders)

    chain = RetrievalQA.from_chain_type(llm=model,
                                        chain_type="stuff",
                                        retriever=index.vectorstore.as_retriever(),
                                        input_key="question")

    response_text = chain.run(question)

    print("--------------------------------- Generated response -----------------------------------")
    print(response_text)
    print("*********************************************************************************************")

    return response_text

if __name__ == "__main__":
    main()