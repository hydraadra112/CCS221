import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity2\nFlood Fill")
fig = plt.figure()

two_d_arr = np.array([[0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1], 
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1]])

st.write('First Plot')
plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
plt.show()
st.pyplot(fig)

st.sidebar.title('ACT 2 - Controls')
color = st.sidebar.slider('Enter Color Number to Fill (0-16):', 0, 16, 1)

for row in range(len(two_d_arr)):
    for col in range(len(two_d_arr)):
      
        if two_d_arr[row][col] == 1:
          continue
          
        if two_d_arr[row][col] == two_d_arr[3][col]:
          plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
          plt.show()
          st.pyplot(fig)

        two_d_arr[row][col] = color
      

plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
plt.show()
st.pyplot(fig)





