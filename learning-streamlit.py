# https://learning-app-ckonar.streamlit.app/
# IDLE file for Python to be used in streamlit
# To make a web app for a calculator 
import streamlit as st   
st.write("Hello")  
st.sidebar.write("Hello") 
"Anything" 
st.title("Nothing")
st.header("Header markdown")
st.markdown("markdown")
st.markdown("## markdown") 
st.header("For Colours")
st.error("Error --red color") 
st.warning("warning --yellow color") 
st.info("Info --blue color") 
st.success("success --green color")
#st.exception("TypeError")  not clear 
st.sidebar.button("Press button", key='1')  
if st.sidebar.button("Press button"):    #--name of the button 
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
st.write("Write any text within triple quote") 
''' Bose was born in Calcutta (now Kolkata), the eldest of seven children in a   
 Bengali Kayastha family.[11] He was the only son, with six sisters after him.      
 His ancestral home was in the village Bara Jagulia, in the district of Nadia,      
 in the Bengal Presidency. His schooling began at the age of five, near his home.    
 When his family moved to Goabagan, he was admitted into the New Indian School.      
 In his final year of school, he was admitted into the Hindu School. He passed       
 his entrance examination (matriculation) in 1909 and stood fifth in the order       
 of merit. He then joined the intermediate science course at the Presidency College,  
 Calcutta, where his teachers included Jagadish Chandra Bose, Sarada Prasanna Das,    
 and Prafulla Chandra Ray. '''  




