import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("Activity 2\nBoundary Fill")
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

st.sidebar.title('ACT 2 - Controls')

color = int(st.sidebar.slider("Enter Color Number to Replace (0-16): ", 0, 16, 1))

row = 0
col = 0

for row in range(len(two_d_arr[row])):
    for col in range(len(two_d_arr[col])):
        
        if two_d_arr[row][col] == 1:
            two_d_arr[row-1][col] = color # above to be changed
            two_d_arr[row][col-1] = color # left to be changed
            
            for row1 in range(1, 5):
                two_d_arr[row1][5] = color
                
            for col1 in range(1, 5):
                two_d_arr[5][col1] = color
                
    plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
    plt.show()
    st.pyplot(fig)
                
    
st.sidebar.write(two_d_arr)
plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
plt.show()
st.pyplot(fig)
        
        
        





