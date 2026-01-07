from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START,StateGraph,END,MessagesState
from langgraph.prebuilt import tool_node,tools_condition
from src.LanGraphAgentic.state.state import State
from src.LanGraphAgentic.node.basic_chatbot_node import BasicChatBotNode



class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph =StateGraph(State)
        
    def Basic_chatbot_build_graph(self):
        """Build Basic chatbot by using langgraph ,BASICCHATBOTNODE, class is intilizer, it have both start and end point
        """   
        self.basic_chatbot_node = BasicChatBotNode(self.llm)
        
        self.graph.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)

        
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.Basic_chatbot_build_graph()
            return self.graph.compile()