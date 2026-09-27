import streamlit as st

st.set_page_config(
    page_title="Salgado Review",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Salgado Midterm Review")
st.write("PHM 516 • Midterm Study Platform")

st.divider()

st.subheader("Question 1")

st.write("Which carbapenem does NOT provide reliable coverage against Pseudomonas aeruginosa?")

answer = st.radio(
    "Choose one:",
    [
        "A. Meropenem",
        "B. Imipenem/cilastatin",
        "C. Ertapenem",
        "D. Doripenem"
    ],
    index=None
)

if st.button("Submit Answer"):
    if answer == "C. Ertapenem":
        st.success("✅ Correct!")
        st.write(
            "**Ertapenem does not reliably cover Pseudomonas, "
            "Acinetobacter, or Enterococcus.**"
        )
    elif answer is None:
        st.warning("Choose an answer first.")
    else:
        st.error("❌ Incorrect. The correct answer is C. Ertapenem.")

st.divider()

st.caption("Salgado Review • PHM 516")
