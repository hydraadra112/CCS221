import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("Activity2\nGroup6\nBoundaryFill")
two_d_arr = np.array([[0, 0, 0, 0, 0, 0], 
                      [0, 1, 1, 1, 1, 0], 
                      [0, 1, 1, 1, 1, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 1, 1, 1, 1, 0], 
                      [0, 0, 0, 0, 0, 0]])

fig = plt.figure()

st.write('Before Boundary Fill')
plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
plt.show()
st.pyplot(fig)

st.write(two_d_arr)

row1 = int(st.number_input("Enter Row (0-2): "))
col1 = int(st.number_input("Enter Index to Replace Color (0-2): "))
color = int(st.number_input("Enter Color Number to Replace (0-16): "))

row = 0
col = 0

for row in range(len(two_d_arr[row])):
    for col in range(len(two_d_arr[col])):
        
        two_d_arr[row1][col1] = color
        
        plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
        plt.show()
        st.pyplot(fig)
        
        
        





