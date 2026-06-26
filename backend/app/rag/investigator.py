from langchain_core.prompts import ChatPromptTemplate

from app.rag.prompts import INVESTIGATOR_PROMPT

from app.rag.retriever import (
    retriever,
    llm,
)

prompt = ChatPromptTemplate.from_template(
    INVESTIGATOR_PROMPT
)


def investigate(question: str):

    docs = retriever.invoke(question)

    print("\nRETRIEVED DOCUMENTS:\n")

    for i, doc in enumerate(docs, 1):
        print(f"\n----- Document {i} -----")
        print(doc.page_content)
        print("Metadata:", doc.metadata)

    if not docs:
        return "The available incident history does not contain enough evidence."

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response.content