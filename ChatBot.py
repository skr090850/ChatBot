import streamlit as st
from langchain_groq import ChatGroq

llm=ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)

st.title("Simpple LLM Chatbot")
st.write("Enter your query below:")
user_input=st.text_input("your question:", "")

if st.button("Get response"):
    response=llm.invoke(user_input)
    st.write("### Response:")
    st.write(response)