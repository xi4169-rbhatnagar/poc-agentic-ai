from dotenv import load_dotenv
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from model import State
from services.node_chatbot import node_chatbot

load_dotenv()

graph_builder = StateGraph(State)
graph_builder.add_node(node_chatbot.__name__, node_chatbot)
graph_builder.add_edge(START, node_chatbot.__name__)
graph_builder.add_edge(node_chatbot.__name__, END)
graph = graph_builder.compile()

print(graph.get_graph().draw_ascii())