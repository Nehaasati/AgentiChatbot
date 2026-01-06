import streamlit as st
import os
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from src.LanGraphAgentic.ui.uiconfig import Config
class LoadStreamUI:
    def __init__(self):
        self.config = Config()
        self.user_controls ={}