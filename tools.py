from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import os

def get_search_tool():
    """Web search tool using Tavily"""
    return TavilySearchResults(
        max_results=5,
        description="Search the web for current information. Use this for any factual questions."
    )

@tool
def summarize_text(text: str) -> str:
    """Summarizes a long piece of text into key points."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = f"Summarize the following text into 5 clear bullet points:\n\n{text}"
    response = llm.invoke(prompt)
    return response.content

@tool  
def calculate(expression: str) -> str:
    """Safely evaluates a basic math expression like '25 * 4 + 10'."""
    try:
        allowed = set("0123456789+-*/()., ")
        if all(c in allowed for c in expression):
            result = eval(expression)
            return f"Result: {result}"
        return "Error: Invalid characters in expression"
    except Exception as e:
        return f"Calculation error: {str(e)}"
