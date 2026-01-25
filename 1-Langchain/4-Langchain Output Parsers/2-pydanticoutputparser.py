from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    
    name: str = Field(description="Person's name")
    age: int = Field(description="Person's age")
    city: str = Field(description="Name of the city person belongs to")
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables = ['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place':'Kalyan'})

print(final_result)