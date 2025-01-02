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
st.header("For Colours")
st.error("Error") 
st.warning("warning") 
st.info("Info") 
st.success("success")
#st.exception("TypeError")  not clear
if st.sidebar.button("Press button"): 
  st.sidebar.write("you have pressed the button")
if st.sidebar.checkbox("Checkbox",value="True"):
  st.sidebar.write("you have checked the box")
  
#------------------------------------------------
#A= st.sidebar.toggle("Toggle")
#if A:
#  st.sidebar.write("on")
#if A == False:
#  st.sidebar.write("off")
#-------------------------------------------------

if st.sidebar.toggle("toggle"):
  st.sidebar.write("On")
else:
  st.sidebar.write("Off") 
A=st.text_input("Write your name", value = "anything") 
if A:
  st.write(f"hello {A}")
def area(x):
  A=3.14*x**2
  return A

R=st.number_input("Write the value of radius",value=3)
if R:
  st.write(area(R))
st.latex(r" \alpha + \beta " )

