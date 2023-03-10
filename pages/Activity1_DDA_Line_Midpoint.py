import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity2\nGroup6\nDDALine_Midpoint")
def DDALine (x1, y1, x2, y2):
    fig = plt.figure
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    steps = max(dx,dy)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    st.write("Midpoint Line:", x3,"&", y3)
    
    Xinc = float (dx / steps)
    Yinc = float (dy / steps)
    
    x = float(x1)
    y = float(y1)
    
    xcords = []
    ycords = []
    
    for i in range (steps):
        xcords.append(x)
        ycords.append(y)
        x += Xinc
        y += Yinc
   
    plt.plot(xcords,ycords,marker="o", markersize=2, markerfacecolor="red")
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="red")
    plt.show()
    st.pyplot(fig)
    
def main () :
    
    x1 = st.slider('X1: ', 0, 100, 1)
    y1 = st.slider('Y1: ', 0, 100, 1)
    x2 = st.slider('X2: ', 0, 100, 1)
    y2 = st.slider('Y2: ', 0, 100, 1)
    DDALine (x1, y1, x2, y2)
    
if __name__ == '__main__':
    main()
            
