import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from orchestrator import run_agents

st.title("Multi-Agent AI Critique System")

prompt = st.text_area("Enter task")

if st.button("Run AI System"):

    if prompt:

        with st.spinner("Running agents..."):

            result = run_agents(prompt)

        st.subheader("Final Output")

        st.write(result)