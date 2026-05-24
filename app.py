import streamlit as st
from agent import ResearchAgent
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(
    page_title="AutoResearch Agent",
    page_icon="🔍",
    layout="wide"
)

st.title("🤖 AutoResearch AI Agent")
st.markdown("*An intelligent agent that searches the web, summarizes, and reasons to answer your questions.*")

# Sidebar info
with st.sidebar:
    st.header("About This Agent")
    st.markdown("""
    **Tools Available:**
    - 🌐 Web Search (Tavily)
    - 📝 Text Summarizer  
    - 🧮 Calculator
    
    **Architecture:**
    - LLM: GPT-3.5-turbo
    - Framework: LangChain
    - Memory: Last 5 turns
    - Agent Type: OpenAI Tools Agent
    """)
    
    if st.button("🗑️ Clear Memory"):
        if "agent" in st.session_state:
            st.session_state.agent.reset_memory()
        st.session_state.messages = []
        st.success("Memory cleared!")

# Initialize agent once (cached)
@st.cache_resource
def load_agent():
    return ResearchAgent()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load agent
agent = load_agent()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("tools_used"):
            st.caption(f"🔧 Tools used: {', '.join(message['tools_used'])}")

# Chat input
if prompt := st.chat_input("Ask me anything... e.g. 'What are the latest AI trends?'"):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("🔍 Researching..."):
            result = agent.run(prompt)
        
        st.markdown(result["answer"])
        
        if result["tools_used"]:
            st.caption(f"🔧 Tools used: {', '.join(result['tools_used'])}")
        
        # Save to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "tools_used": result["tools_used"]
        })
