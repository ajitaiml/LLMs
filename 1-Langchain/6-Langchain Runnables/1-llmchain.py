from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain  ## DEPRECIATED CAN'T USE IT NOW
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # use chat model
    temperature=0.7 
)

# Simple prompt
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}."
)

# chain = LLMChain(llm=llm, prompt=prompt)

# result = chain.run("LangChain and AI")
# print(result)
