# 🤖 AutoResearch AI Agent

An intelligent AI agent that answers research questions by searching the web, 
summarizing content, and performing calculations — with full conversation memory.

## 🎯 Problem Solved
Traditional chatbots can't access real-time information and have no tools. 
This agent dynamically decides which tool to use, when to use it, and 
how to combine results to give accurate, cited answers.

## 🏗️ Architecture
User Question → AgentExecutor (LangGraph) → LLM decides which tool to call
→ Tool 1: Tavily Web Search
→ Tool 2: Text Summarizer  
→ Tool 3: Calculator
→ Agent synthesizes results → Final Answer with sources

## ⚙️ Setup Instructions

### 1. Clone the repo
git clone https://github.com/dnyaneshwari102003/autoresearch-agent.git
cd autoresearch-agent

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up API keys in .env file
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here

### 5. Run the app
streamlit run app.py

## 🔑 Key Engineering Challenge
Preventing infinite tool loops and model hallucination.
Solved with max_iterations=5 and temperature=0.

## 🛠️ Tech Stack
- LangChain + LangGraph — Agent framework
- Groq LLaMA 3.3 — Core LLM (free and fast)
- Tavily — Real-time web search
- Streamlit — UI
