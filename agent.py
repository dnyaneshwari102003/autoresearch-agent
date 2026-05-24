from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools import get_search_tool, summarize_text, calculate
from dotenv import load_dotenv
import os

load_dotenv()

class ResearchAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )
        
        self.tools = [
            get_search_tool(),
            summarize_text,
            calculate
        ]
        
        self.agent = create_react_agent(
            model=self.llm,
            tools=self.tools
        )
        
        self.chat_history = []
    
    def run(self, question: str) -> dict:
        try:
            self.chat_history.append({"role": "user", "content": question})
            
            result = self.agent.invoke({
                "messages": self.chat_history
            })
            
            answer = result["messages"][-1].content
            self.chat_history.append({"role": "assistant", "content": answer})
            
            return {
                "answer": answer,
                "tools_used": [],
                "success": True
            }
        except Exception as e:
            return {
                "answer": f"Agent encountered an error: {str(e)}",
                "tools_used": [],
                "success": False
            }
    
    def reset_memory(self):
        self.chat_history = []


if __name__ == "__main__":
    agent = ResearchAgent()
    
    test_questions = [
        "What is LangChain and what is it used for?",
        "What is 15% of 2500?",
        "Who founded OpenAI and when?"
    ]
    
    for q in test_questions:
        print(f"\n{'='*50}")
        print(f"Question: {q}")
        result = agent.run(q)
        print(f"Answer: {result['answer']}")
