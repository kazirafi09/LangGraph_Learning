from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START, END

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

def draft_node(state: MessagesState):
    prompt = "Write a 3 line poem or a 3 line joke"
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": [response]}

def critique_node(state: MessagesState):
    last_draft = state["messages"][-1].content
    
    prompt = f"Evaluate this draft and suggest one concrete improvement:\n\n{last_draft}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": [response]}

def print_node(state: MessagesState):
    last_msg = state["messages"][-1]
    
    print("--- Final Output ---")
    if isinstance(last_msg.content, str):
        print(last_msg.content)
    elif isinstance(last_msg.content, list):
        print(last_msg.content[0]["text"])
    return {}


graph_builder = StateGraph(MessagesState)

graph_builder.add_node("draft_node", draft_node)
graph_builder.add_node("critique_node", critique_node)
graph_builder.add_node("print_node", print_node)

graph_builder.add_edge(START, "draft_node")
graph_builder.add_edge("draft_node", "critique_node")
graph_builder.add_edge("critique_node", "print_node")
graph_builder.add_edge("print_node", END)

app = graph_builder.compile()
app.invoke({"messages": []})