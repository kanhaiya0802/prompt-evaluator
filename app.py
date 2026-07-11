import streamlit as st

from utils.gemini import evaluate_prompt
from utils.helpers import parse_response


st.set_page_config(
    page_title="Prompt Evaluator",
    layout="wide"
)

st.title("Prompt Evaluator")
st.caption("Evaluate and improve your prompts using Google Gemini")

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Write or paste your prompt here...",
    height=300
)

if st.button("Evaluate Prompt", use_container_width=True):

    if not prompt.strip():
        st.warning("Please enter a prompt.")

    else:
        try:
            with st.spinner("Evaluating prompt..."):

                response = evaluate_prompt(prompt)
                result = parse_response(response)

            st.success("Evaluation completed successfully.")

            st.divider()

            st.subheader("Overall Score")

            st.metric(
                "Overall Score",
                f'{result["overall_score"]}/100'
            )
            st.progress(result["overall_score"] / 100)

            st.divider()

            st.subheader("Category Scores")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Clarity", result["clarity"])
                st.metric("Context", result["context"])
                st.metric("Output Format", result["output_format"])
                st.metric("Tone", result["tone"])

            with col2:
                st.metric("Specificity", result["specificity"])
                st.metric("Constraints", result["constraints"])
                st.metric("Examples", result["examples"])

            st.divider()

            st.subheader("Strengths")

            for strength in result["strengths"]:
                st.info(strength)

            st.divider()

            st.subheader("Weaknesses")

            for weakness in result["weaknesses"]:
                st.warning(weakness)

            st.divider()

            st.subheader("Suggestions")

            for suggestion in result["suggestions"]:
                st.success(suggestion)

            st.divider()

            with st.container(border=True):
                st.subheader("Improved Prompt")

                st.text_area(
                    "Improved Prompt",
                    value=result["improved_prompt"],
                    height=300
                )

        except Exception as error:
            st.error(f"Error: {error}")