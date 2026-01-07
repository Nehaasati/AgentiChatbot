from typing import Literal,TypedDict,Annotated,Optional
from langchain_core.messages import ChatMessage,AIMessage,HumanMessage
from langgraph.graph.message import add_messages
class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[list, add_messages]