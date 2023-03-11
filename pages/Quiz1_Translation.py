import matplotlib.pyplot as plt
import numpy as np
import cv2 
import streamlit as st

st.title('Quiz1\nGroup6')

def firstTranslate(bx, by, img, rows, cols):
    
    m_translation_ = np.float32([[1, 0, bx],
                                 [0, 1, by],
                                 [0, 0, 1]]) 

    img_ = cv2.warpPerspective(img, m_translation_, (rows, cols))

    print(m_translation_)
    return img_

def translation(img, bx, by, tx, ty, rows, cols):

    Tx_new = bx + tx
    Ty_new = by + ty

    m_translation_ = np.float32([[1, 0, Tx_new],
                                 [0, 1, Ty_new],
                                 [0, 0, 1]]) 

    translated_img_ = cv2.warpPerspective(img, m_translation_, (rows, cols))

    print(m_translation_)
    return translated_img_

def main():
    
    fig = plt.figure()
    
    
    address = str("C:/Users/admin/Desktop/Shes/")
    i = st.slider('Choose Picture', 1, 3, 1)
        
    img = cv2.imread(address + str(i) + ".jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.write('First and Second Positions by Images:')
    
    bx = st.slider('First Position Bx: ', 1, 500, 1)
    by = st.slider('First Position By: ', 1, 500, 1)

    tx = st.slider('Second Position Bx: ', 1, 500, 1)
    ty = st.slider('Second Position By: ', 1, 500, 1)

    rows, cols = (img.shape[:2])
    
    st.write('First Position')
    first_translation_ = firstTranslate(bx,by,img, rows, cols)
    plt.axis('off')
    plt.imshow(first_translation_)
    plt.show()
    st.pyplot(fig)
    
    
    st.write("Second Position")
    translated_image = translation(img, bx, by, tx, ty, rows, cols)
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
