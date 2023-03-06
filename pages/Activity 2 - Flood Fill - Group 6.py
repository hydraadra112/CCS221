import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[0, 1, 0], 
                    [1, 1, 1], 
                    [0, 1, 0]])

color = int(input("Enter Color Number to Fill (0-16): "))

for row in range(len(two_d_arr)):
    for col in range(len(two_d_arr)):
        two_d_arr[row][col] = color
        print(two_d_arr)
        plt.imshow(two_d_arr, interpolation='none', cmap='gray_r')
        plt.show()





