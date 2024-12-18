# IDLE file for Python to be used in streamlit
# To make a web app for a calculator 
import streamlit as st  
st.write("hello")  
st.sidebar.write("Hello") 
"Anything" 
st.title("Nothing")
st.header("Header")
st.markdown("markdown")
st.markdown("## markdown") 
st.error("Error") 
st.warning("warning") 
st.info("Info") 
st.success("success")
#st.exception("TypeError")  not clear
if st.sidebar.button("Press button"): 
  st.sidebar.write("you have pressed the button")
if st.sidebar.checkbox("Checkbox",value="True"):
  st.sidebar.write("you have checked the box")
A= st.sidebar.toggle("Toggle")
if A:
  st.sidebar.write("on")
if A == False:
  st.write("off")
