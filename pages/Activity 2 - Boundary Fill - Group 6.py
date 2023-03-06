
import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[0, 0, 1, 1, 0, 0], 
                      [0, 1, 0, 0, 1, 0], 
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0], 
                      [0, 0, 1, 1, 0, 0]])

print(two_d_arr)

row = 0
col = 0

for row in range(len(two_d_arr[row])):
    for col in range(len(two_d_arr[col])):
        
        row1 = int(input("Enter Row (0-2): "))
        col1 = int(input("Enter Index to Replace Color (0-2): "))
        color = int(input("Enter Color Number to Replace (0-16): "))
        
        two_d_arr[row1][col1] = color
        print(two_d_arr)
        
        plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
        plt.show()
        
        again = int(input("\n1 to Change, 2 to Finish: "))
        if again == 2:
            plt.imshow(two_d_arr, interpolation='none', cmap='Set3')
            plt.show()
            
            break
        
    if again == 2:
            break





