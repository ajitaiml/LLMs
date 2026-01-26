from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description="Give the sentiment of the Feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text positve or negative \n {feedback}\n{format_instructions}",
    input_variables = ['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)    

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to ths=is negatice feedback \n {feedback}",
    input_variables= ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "Positive",prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': "this phone is great but it's camera is bad"}))

chain.get_graph().print_ascii()
