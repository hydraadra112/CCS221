import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity2\nGroup6\nFloodFill")
fig = plt.figure()

two_d_arr = np.array([[0, 1, 0], 
                    [1, 1, 1], 
                    [0, 1, 0]])


color = st.slider('Enter Color Number to Fill (0-16):' 0, 16, 1)

for row in range(len(two_d_arr)):
    for col in range(len(two_d_arr)):
        two_d_arr[row][col] = color
        plt.imshow(two_d_arr, interpolation='none', cmap='gray_r')
        plt.show()
        st.pyplot(fig)





