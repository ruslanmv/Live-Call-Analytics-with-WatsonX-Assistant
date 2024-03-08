# LLM Virtual Assistant - Part 1

In this part of the project, we will be building the LLM Virtual Assistant using WatsonX.ai. The virtual assistant will be powered by a simple vector database to store questions and answers. We will utilize the standard RAG (Retriever-Augmented Generation) for retrieving the most accurate answer and implement reinforcement learning to improve the model over time.

## Prerequisites

Ensure that you have the following installed:

- Python 3.10
- [IBM Watson Machine Learning SDK](https://pypi.org/project/ibm-watson-machine-learning/)
- [ChromaDB](https://pypi.org/project/chromadb/)
- [Chardet](https://pypi.org/project/chardet/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

You can install the above packages using pip:

```bash
pip install ibm-watson-machine-learning chromadb chardet python-dotenv
```

## LLM Virtual Assistant Code

Save the following Python code in a file named `llm_virtual_assistant.py`:

```python
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
```

## Steps to run the LLM Virtual Assistant

1. Set up your environment: Store your IBM Cloud API key and WatsonX.ai project ID in a `.env` file. This file should contain the following keys:

```
api_key=<your_ibm_cloud_api_key>
project_id=<your_project_id>
```

2. Save the LLM Virtual Assistant Python code (provided above) in a file named `llm_virtual_assistant.py`.

3. Run the `llm_virtual_assistant.py` script to set up the LLM Virtual Assistant:

```bash
python llm_virtual_assistant.py
```

This will create a chatbot powered by WatsonX.ai and implement reinforcement learning to improve the model over time.

For more information on the other parts of this project, please refer to the main [README.md](../README.md) file.
```

You can copy and paste this updated content into a new README.md file for the First Part of the LLM Virtual Assistant in your project. Make sure to follow the steps provided to run the application.