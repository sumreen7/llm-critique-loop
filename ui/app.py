import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from orchestrator import run_agents

st.title("Multi-Agent Resume Tailoring System")
st.caption("Writer → Critic → Editor → Judge — loops until approved")

st.markdown("""
**Paste your input in this exact format:**
```
JD:
<paste job description here>

RESUME:
<paste your LaTeX resume here>
```
""")

prompt = st.text_area("Input", height=400)

if st.button("Run"):
    if prompt:
        iteration_box = st.empty()
        
        with st.spinner("Running agents..."):
            result, history = run_agents(prompt)

        st.subheader("Iteration History")
        for h in history:
            with st.expander(f"Iteration {h['iteration']} — Score: {h['score']}/10"):
                col1, col2, col3 = st.columns(3)
                col1.metric("Overall", f"{h['score']}/10")
                col2.metric("Language Fit", f"{h['language_alignment_score']}/10")
                col3.metric("Quality", f"{h['quality_score']}/10")
                st.write(f"**Issues found:** {h['issues_count']}")
                if h['missing_keywords']:
                    st.write(f"**Missing JD keywords:** {', '.join(h['missing_keywords'])}")
                st.write(f"**Feedback:** {h['feedback']}")

        st.subheader("Final Resume (LaTeX)")
        st.code(result, language="latex")
        
        st.download_button(
            "Download LaTeX",
            data=result,
            file_name="tailored_resume.tex",
            mime="text/plain"
        )