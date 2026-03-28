import streamlit as st
from src.main import run_system

st.title("🚀 AI Digital Twin Dashboard")

query = st.text_input("Enter Business Query")

marketing = st.slider("Marketing Spend", 10000, 50000, 20000)
ops = st.slider("Operations Cost", 5000, 20000, 10000)

if st.button("Run Simulation"):
    result = run_system(query, marketing, ops)
    
    st.write("### 📊 Results")
    st.write(f"Predicted Revenue: {result['prediction']:.2f}")
    st.write(f"Growth: {result['growth']:.2f}%")
    st.write(f"Decision: {result['decision']}")
    
    st.write("### 🧠 Insights (RAG)")
    for i in result['insights']:
        st.write("-", i)