import matplotlib.pyplot as plt
import numpy as np
import cv2 
import streamlit as st
from PIL import Image

st.title('Quiz 1')


def firstTranslate(bx, by, img, rows, cols):
    
    m_translation_ = np.float32([[1, 0, bx],
                                 [0, 1, by],
                                 [0, 0, 1]]) 

    img_ = cv2.warpPerspective(img, m_translation_, (rows, cols))
    return img_

def translation(img, bx, by, tx, ty, rows, cols):

    Tx_new = bx + tx
    Ty_new = by + ty

    m_translation_ = np.float32([[1, 0, Tx_new],
                                 [0, 1, Ty_new],
                                 [0, 0, 1]]) 

    translated_img_ = cv2.warpPerspective(img, m_translation_, (rows, cols))
    return translated_img_

def main():
    
    fig = plt.figure()
    img_ = st.file_uploader('Upload Image to Use in Order for the Program to Work', ['jpg'], accept_multiple_files=False)
    
    img_ = Image.open(img_)
    img_ = np.asarray(img_)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
    
    st.sidebar.title('QUIZ 1 - Controls')
    bx = st.sidebar.slider('1ST Bx: ', 1, 500, 1)
    by = st.sidebar.slider('1ST By: ', 1, 500, 1)

    tx = st.sidebar.slider('2ND Bx: ', 1, 500, 1)
    ty = st.sidebar.slider('2ND By: ', 1, 500, 1)

    rows, cols = (img_.shape[:2])
    
    st.write('First Position')
    first_translation_ = firstTranslate(bx, by, img_, rows, cols)
    plt.axis('off')
    plt.imshow(first_translation_)
    plt.show()
    st.pyplot(fig)
    
    
    st.write("Second Position")
    translated_image = translation(img_, bx, by, tx, ty, rows, cols)
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
