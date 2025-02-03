from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv("/Users/kumarswamikallimath/Desktop/GenAI/.env")
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=GROQ_API_KEY
)

# Function to get the states
def get_states(count : str):

    prompt =PromptTemplate(
        input_variables = ['country'],
        template = "Only list the sates of {country}"
    )

    formatted_prompt = prompt.format(country=count)
    response = llm.invoke(formatted_prompt)

    return response.content


