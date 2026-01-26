from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

# Load environment variables (your OPENAI_API_KEY should be in .env)
load_dotenv()

# Initialize the semantic text splitter
text_splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",  # or "percentile", etc.
    breakpoint_threshold_amount=0
)

# The sample text
sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

# Create documents
docs = text_splitter.create_documents([sample])

# Output
print("Number of chunks:", len(docs))
for idx, doc in enumerate(docs, start=1):
    print(f"\n--- Chunk {idx} ---")
    print(doc.page_content)
