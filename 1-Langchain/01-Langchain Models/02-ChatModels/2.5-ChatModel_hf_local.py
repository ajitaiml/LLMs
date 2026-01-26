from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch

# Select GPU if available, else CPU
device = 0 if torch.cuda.is_available() else -1

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    device=device,  # 👈 this enables GPU
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Nepal?")
print(result)
