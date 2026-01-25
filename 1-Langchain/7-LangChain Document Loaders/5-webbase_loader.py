from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template = "Answer the following questions \n {question} from the following text -\n {text}",
    input_variables = ['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/Kreo-Swarm-Wireless-Mechanical-Keyboard/dp/B0FLKD14YD/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':' What is the product that we are taking about?','text':docs[0].page_content}))