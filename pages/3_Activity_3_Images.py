import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
st.title("Activity3\nGroup6\nImages")
# Reading of Image
jpg = str(".jpg")
fig = plt.figure()
address = str("pages/")

def translation(i,x,y):
    
    #Translation
    m_translation_ = np.float32([[1, 0, x],
                                 [0, 1, y],
                                 [0, 0, 1]])
    
 
    img_ = cv2.imread(address + str(i) + jpg)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    cols, rows = (img_.shape[:2])

    translated_img_ = cv2.warpPerspective(img_, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_img_)
    plt.show()
    st.pyplot(fig)

def rotation(i, angle):
    
    # Rotation
    angle = np.radians(angle)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    
   
    img_ = cv2.imread(address + str(i) + jpg)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    cols, rows = img_.shape[:2] 

    rotated_img_ = cv2.warpPerspective(img_, m_rotation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(rotated_img_)
    plt.show()
    st.pyplot(fig)
    
def scaling(i,x,y):
    
    # Scaling
    
    m_scaling_ = np.float32([[y, 0, 0],
                             [0, x, 0],
                             [0, 0, 1]])
    
   
    img_ = cv2.imread(address + str(i) + jpg)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    cols, rows = img_.shape[:2] 

    scaled_img_ = cv2.warpPerspective(img_, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_img_)
    plt.show()
    st.pyplot(fig)
    
def shear(i):
    
    # Shearing
    m_shearing_x = np.float32([[1, 0.5, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
    
    
    img_ = cv2.imread(address + str(i) + jpg)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    cols, rows = img_.shape[:2]

    sheared_img_x = cv2.warpPerspective(img_,m_shearing_x,(int(cols*1.5), int(rows*1.5)))
    plt.axis('off')
    plt.imshow(sheared_img_x)
    plt.show()
    st.pyplot(fig)

def reflection(i):
    
    # Reflection
    
    img_ = cv2.imread(address + str(i) + jpg)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    cols, rows = img_.shape[:2]
    
    m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]])
    
  

    reflected_img_ = cv2.warpPerspective(img_, m_reflection_,(int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(reflected_img_)
    plt.show()
    st.pyplot(fig)

def main () :
    i = st.slider('Choose Image (1-3)', 1, 3, 1)
    
    method = st.multiselect('Choose Manipulation Method', ['Translation', 'Rotation', 'Scale', 'Shear', 'Reflection'], ['Translation'])
  
    
    if 'Translation' in method:
        x = st.slider('X Translation', 0, 500, 1)
        y = st.slider('Y Translation', 0, 500, 1)
        st.write("Translation")
        translation(i,x,y)
    
    if 'Rotation' in method:
        angle = st.slider('Rotation Size', 0, 500, 1)
        st.write("Rotation")
        rotation(i, angle)
        
    if 'Scale' in method:
        x = float(st.slider('X Translation', 0, 5, 0.1))
        y = float(st.slider('Y Translation', 0, 5, 0.1))
        st.write("Scale")
        scaling(i,x,y)
    
    if 'Shear' in method:
        st.write("Shear")
        shear(i)
    
    if 'Reflection' in method:
        st.write("Reflection")
        reflection(i)
    
    
if __name__ == '__main__':
    main()
