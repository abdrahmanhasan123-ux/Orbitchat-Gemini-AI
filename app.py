import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini
# Replace 'YOUR_API_KEY' with your actual key from https://aistudio.google.com/
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Initialize Session State (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🚀 OrbitChat AI")
st.markdown("A simple AI with memory.")

# 3. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input
if prompt := st.chat_input("Ask me anything..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        # We pass the history so the AI 'remembers' previous turns
        full_history = [{"role": m["role"], "parts": [m["content"]]} for m in st.session_state.messages]
        response = model.generate_content(contents=full_history)
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
