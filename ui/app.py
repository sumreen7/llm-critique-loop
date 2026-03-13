import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from loop import run_loop

st.title("Multi-LLM Critique Loop")

st.write("ChatGPT generates → Claude critiques → loop until approval")

prompt = st.text_area("Enter your prompt")

if st.button("Run Critique Loop"):

    if prompt:

        with st.spinner("Running critique loop..."):

            result = run_loop(prompt)

        st.subheader("Final Output")
        st.write(result)