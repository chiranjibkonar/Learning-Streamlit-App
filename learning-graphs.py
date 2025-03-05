# learning graphs
# https://learning-app-graphs-ckonar.streamlit.app/
import matplotlib.pyplot as plt
import numpy as np 
import streamlit as st 

x=np.linspace(10,100,10)  # Explanation: Along x axis: 1st value = start value, 2nd value = end value, 3rd value is the number of points 
y=[i**2 for i in x] 
st.write(f"x values are: {x}")   # f means formatted string, 
st.write(f"yvalues are: {y}")    
fig=plt.figure()
plt.plot(x,y)
st.pyplot(fig)


