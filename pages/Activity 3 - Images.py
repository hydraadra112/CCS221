import numpy as np
import cv2
import matplotlib.pyplot as plt

# Reading of Image
i = int(1)
jpg = str(".jpg")
address = str("C:/Users/admin/Desktop/PROG/python_acts/python_exercises/")

img_ = cv2.imread(str(i) + jpg)
img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
cols, rows = img_.shape[:2]

def translation():
    
    #Translation
    m_translation_ = np.float32([[1, 0, 100],
                                 [0, 1, 200],
                                 [0, 0, 1]])
    
    for i in range(1, 5):
        img_ = cv2.imread(address + str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = (img_.shape[:2])
        
        translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows))
        plt.axis('off')
        plt.imshow(translated_img_)
        plt.show()

def rotation():
    
    # Rotation
    angle = np.radians(10)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    
    for i in range(1, 5):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2] 
        
        rotated_img_ = cv2.warpPerspective(img_, m_rotation_, (int(cols), int(rows)))
        plt.axis('off')
        plt.imshow(rotated_img_)
        plt.show()
    
def scaling():
    
    # Scaling
    m_scaling_ = np.float32([[1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]])
    
    for i in range(1, 5):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2] 
    
        scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (cols*2, rows*2))
        plt.axis('off')
        plt.imshow(scaled_img_)
        plt.show()
    
def shear():
    
    # Shearing
    m_shearing_x = np.float32([[1, 0.5, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    
    for i in range(1, 5):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]
    
        sheared_img_x = cv2.warpPerspective(img_,m_shearing_x,(int(cols*1.5), int(rows*1.5)))
        plt.axis('off')
        plt.imshow(sheared_img_x)
        plt.show()

def reflection(rows):
    
    # Reflection
    m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]])
    
    for i in range(1, 5):
        img_ = cv2.imread(str(i) + jpg)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        cols, rows = img_.shape[:2]
    
        reflected_img_ = cv2.warpPerspective(img_, m_reflection_,(int(cols), int(rows)))
        plt.axis('off')
        plt.imshow(reflected_img_)
        plt.show()

def main () :
    print("Translation  :: 1")
    print("Rotation     :: 2")
    print("Scaling      :: 3")
    print("Shear        :: 4")
    print("Reflection   :: 5")
    choice = int(input("Input Choice :: "))
    
    again = "y"
    
    while(again == "y"):
        
        if choice == 1:
            translation()
        
        elif choice == 2:
            rotation()
        
        elif choice == 3:
            scaling()
        
        elif choice == 4:
            shear()
        
        elif choice == 5:
            reflection(rows)
            
        again = str(input("Continue (y/n): "))
        
        if again == "n":
            exit()
        
        print("Translation  :: 1")
        print("Rotation     :: 2")
        print("Scaling      :: 3")
        print("Shear        :: 4")
        print("Reflection   :: 5")
        choice = int(input("Input Choice :: "))
        

    
if __name__ == '__main__':
    main()