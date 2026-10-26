from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

#load env
load_dotenv()
llm = ChatOpenAI()


#create state
class  ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]

#checkpointer
checkpointer = InMemorySaver()

#node function
def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}
# graph creation
graph = StateGraph(ChatState)

#node making as function

graph.add_node('chat_node',chat_node)
graph.add_edge(START ,"chat_node")
graph.add_edge("chat_node",END)

# call compiler 
chatbot = graph.compile(checkpointer=checkpointer)