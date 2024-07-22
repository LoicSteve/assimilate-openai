from oalib.solutions import code_generator
import streamlit as st # type: ignore

st.title("🕹️ AI Code Generator Web App")
st.write("convert comments to code in multiple languages")

language = st.selectbox("Select Language", ["python", "javascript", "java", "c++", 'c#', 'ruby', 'go', 'swift', 'php', 'sql', 'typescript', 'kotlin', 'rust', 'scala', 'r', 'perl', 'haskell', 'shell', 'julia', 'dart', 'elixir'])
text = st.text_input("Input Question 👇")

if st.button("Generate Code"):
    with st.spinner("In progress"):
        response = code_generator(text, language)
        st.code(response, language=language)