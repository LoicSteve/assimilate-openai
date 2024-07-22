import streamlit as st
from oalib.solutions import submit_question

# Get the OpenAI API Key
api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

# Setting up the Title
st.title("🕹️ AI Question Answering Bot")

st.write(
    "_**Intelligent QA bot that will answer all your questions in zero shot based on the context from the internet.**_"
)

QUESTION = st.text_input("Input Question 👇")

@st.cache
def cached_submit_question():
    return submit_question

submit_question_cached = cached_submit_question()

if st.button("Submit"):
    st.write("**Output**")
    st.write("""---""")
    with st.spinner(text="In progress"):
        report_text = submit_question_cached(QUESTION)
        st.markdown(report_text)