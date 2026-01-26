from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

## Initiate the LLM model
model = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.7)

## Create a prompt template
prompt = PromptTemplate(
    input_variables = ['topic'],
    template="Suggest a catchy blog title about {topic}"
)

# Define the input
topic = input("Enter the Topic")

# Format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

# Call the promt manually using PromptTemplate
blog_title = model.invoke(formatted_prompt)

# Print the output
print("Generated Blog Title: ",blog_title)