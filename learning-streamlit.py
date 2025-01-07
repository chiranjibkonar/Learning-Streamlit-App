# https://learning-app-ckonar.streamlit.app/
# IDLE file for Python to be used in streamlit
# To make a web app for a calculator 
import streamlit as st   
st.write("Hello")  
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
st.write(r"$ \frac{\alpha + \beta}{\gamma + \delta} $" )
col1, col2=st.columns(2)
with col1:
  st.write("col1") 
  st.button("1") 
with col2:
  st.write("col2")
  st.button("2")
st.write("Write a text below") 
st.markdown("<div style='text-align: left;'> \
Bose was born in. </div>", \
unsafe_allow_html=True) 

"" line 1 \
line 2 ""
