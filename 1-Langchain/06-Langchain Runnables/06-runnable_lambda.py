from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

# Prompts
joke_prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

explain_prompt = PromptTemplate(
    template="Explain the following joke in simple words:\n{text}",
    input_variables=["text"]
)

model = ChatOpenAI()
parser = StrOutputParser()

# Step 1: joke generator
joke_chain = joke_prompt | model | parser

# Step 2: parallel branches
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": (
        {"text": RunnablePassthrough()}
        | explain_prompt
        | model
        | parser
    ),
    "word count": RunnableLambda(word_count)
})

# Step 3: full chain
final_chain = joke_chain | parallel_chain

# Execute
result = final_chain.invoke({"topic": "AI"})

# Output formatting
final_output = f"""
Joke:
{result['joke']}

Explanation:
{result['explanation']}

Word count: {result['word count']}
"""

print(final_output)
