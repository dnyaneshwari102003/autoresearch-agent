from langchain.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
import os

class AgentMemory:
    """Manages short-term and long-term memory for the agent"""
    
    def __init__(self):
        self.short_term = ConversationBufferWindowMemory(
            k=5,  # Remember last 5 exchanges
            memory_key="chat_history",
            return_messages=True
        )
        self.research_history = []
    
    def save_research(self, question: str, answer: str):
        """Save a research result to history"""
        self.research_history.append({
            "question": question,
            "answer": answer
        })
    
    def get_history(self):
        return self.research_history
    
    def clear(self):
        self.short_term.clear()
        self.research_history = []
