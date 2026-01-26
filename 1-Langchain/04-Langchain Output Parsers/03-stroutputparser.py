from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name='fact1',description='fact1 about the topic'),
    ResponseSchema(name='fact2',description='fact2 about the topic'),
    ResponseSchema(name='fact3',description='fact3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me 3 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser
    
result = chain.invoke({'topic':'black hole'})

print(result)



# IMP -> DEPRECIATED IN LANGCHAIN CANT USE IT ANYMORE