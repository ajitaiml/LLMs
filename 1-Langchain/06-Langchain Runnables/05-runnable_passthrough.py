from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=["text"]
)

# Step 1: joke generation
joke_gen_chain = prompt1 | model | parser

# Step 2: parallel branching
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": (
        {"text": RunnablePassthrough()}
        | prompt2
        | model
        | parser
    )
})

# Step 3: full pipeline
final_chain = joke_gen_chain | parallel_chain

# Execute
result = final_chain.invoke({"topic": "Cricket"})

print("Joke:")
print(result["joke"])

print("\nExplanation:")
print(result["explanation"])
