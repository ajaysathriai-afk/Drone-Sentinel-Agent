from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

vectorstore = Chroma(
    collection_name="incidents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 20
    }
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
