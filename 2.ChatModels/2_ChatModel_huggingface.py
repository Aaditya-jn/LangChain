from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(

    repo_id = "google/gemma-3-4b-it",
    task = "text-generation"

)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Who is the Prime Minister of Russia and India")

print(result)