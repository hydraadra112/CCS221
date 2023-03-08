import streamlit as st
import matplotlib.pyplot as plt

st.title("Activity1\nGroup6\nBresenhamMidpoint")

def DDALine (x1, y1, x2, y2, color):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    print("Midpoint Line:", x3,"&", y3)
    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    for i in range (0, int(steps+1)):
        st.line_chart(int(x1), int(y1))
        x1 += Xinc
        y1 += Yinc
        
    st.pyplot(x3,y3,marker="o", markersize=5, markerfacecolor="r")
    plt.show()
    
def main () :
    x1 = st.number_input('X1: ')
    y1 = st.number_input('Y1: ')
    x2 = st.number_input('X2: ')
    y2 = st.number_input('Y2: ')
    color = "b."
    DDALine (x1, y1, x2, y2, color)
    
    x1 = 10
    y1 = 15
    x2 = 45
    y2 = 67
    
    #Enter X1: 10
    #Enter Y1: 15
    #Enter X2: 45
    #Enter Y2: 67 
    
if __name__ == '__main__':
    main()
            
