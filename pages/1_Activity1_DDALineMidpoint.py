import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity2\nGroup6\nDDALine_Midpoint")

def DDALine (x1, y1, x2, y2, color):
    fig = plt.figure()
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    st.write("Midpoint Line:", x3,"&", y3)
    
    if abs(dx) > abs(dy):
        steps = abs(dx)
    
    else:
        steps = abs(dy)
        
    
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    for i in range (0, int(steps+1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="r")
    plt.show()
    st.pyplot(fig)
    
def main () :
    x1 = st.slider('X1: ', 0, 100, 1)
    y1 = st.slider('Y1: ', 0, 100, 1)
    x2 = st.slider('X2: ', 0, 100, 1)
    y2 = st.slider('Y2: ', 0, 100, 1)
    color = "b."
    DDALine (x1, y1, x2, y2, color)
    
    #Enter X1: 10
    #Enter Y1: 15
    #Enter X2: 45
    #Enter Y2: 67 
    
if __name__ == '__main__':
    main()