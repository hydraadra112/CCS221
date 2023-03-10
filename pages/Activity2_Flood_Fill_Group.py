import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity2\nGroup6\nFloodFill")
fig = plt.figure()

two_d_arr = np.array([[0, 0, 0, 0],
                    [0, 1, 1, 0], 
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]])

st.write('First Plot')
plt.imshow(two_d_arr, interpolation='none', cmap='inferno')
plt.show()
st.pyplot(fig)

color = st.slider('Enter Color Number to Fill (0-16):', 0, 16, 1)

for row in range(len(two_d_arr)):
    for col in range(len(two_d_arr)):
      
        if two_d_arr[row][col] == 1:
          continue
          
        two_d_arr[row][col] = color

st.write('Second Plot with Color Changed')
plt.imshow(two_d_arr, interpolation='none', cmap='inferno')
plt.show()
st.pyplot(fig)





