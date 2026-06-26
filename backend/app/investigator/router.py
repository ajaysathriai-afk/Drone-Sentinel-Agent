from langchain_openai import ChatOpenAI

from app.investigator.sql_agent import sql_investigate
from app.rag.investigator import investigate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def investigate_question(question: str):

    prompt = f"""
You are an intent classifier.

Classify the user's question into exactly ONE category.

Return ONLY one word.

sql -> counting, aggregation, statistics, reports, summaries, totals

rag -> explanations, descriptions, incidents, image questions, reasoning

Question:
{question}
"""

    intent = llm.invoke(prompt).content.strip().lower()

    print(f"\nLLM Intent: {intent}\n")

    if intent == "sql":
        return sql_investigate(question)

    return investigate(question)
