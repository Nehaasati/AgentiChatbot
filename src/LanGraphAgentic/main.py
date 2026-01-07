import streamlit as st
import json
from src.LanGraphAgentic.ui.stremlitui.load_ui import LoadStreamlitUI
from src.LanGraphAgentic.LLM.groqllm import GroqLLM
from src.LanGraphAgentic.graph.graph_builder import GraphBuilder
from src.LanGraphAgentic.ui.stremlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    """
    print("=== Starting LangGraph Agentic AI App ===")
    
    try:
        # Load UI
        ui = LoadStreamlitUI()
        user_input = ui.load_streamlit_ui()
        
        print(f"User input loaded: {user_input}")

        if not user_input:
            st.error("Error: Failed to load user input from the UI.")
            return

        # Text input for user message
        if st.session_state.IsFetchButtonClicked:
            user_message = st.session_state.timeframe 
        else:
            user_message = st.chat_input("Enter your message:")

        if user_message:
            print(f"User message received: {user_message}")
            
            try:
                # Configure LLM
                print("Configuring LLM...")
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()
                
                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    print("ERROR: Model is None")
                    return
                
                print("LLM model configured successfully")

                # Initialize and set up the graph based on use case
                usecase = user_input.get('selected_usecase')
                print(f"Selected usecase: {usecase}")
                
                if not usecase:
                    st.error("Error: No use case selected.")
                    return
                
                # Build graph
                print("Building graph...")
                graph_builder = GraphBuilder(model)
                
                try:
                    graph = graph_builder.setup_graph(usecase)
                    
                    if not graph:
                        st.error("Error: Graph setup returned None")
                        print("ERROR: Graph is None")
                        return
                    
                    print("Graph setup completed successfully")
                    
                    # Display result
                    print("Displaying result...")
                    DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
                    print("Result displayed successfully")
                    
                except Exception as e:
                    error_msg = f"Error: Graph setup failed - {e}"
                    print(error_msg)
                    st.error(error_msg)
                    return
                    
            except Exception as e:
                error_msg = f"Error in message processing: {e}"
                print(error_msg)
                st.error(error_msg)
                raise
                
    except Exception as e:
        error_msg = f"Error Occurred with Exception: {e}"
        print(error_msg)
        st.error(error_msg)
        raise