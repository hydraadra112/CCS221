import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity2\nGroup6\nDDALine_Midpoint")
def DDALine (x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    steps = max(dx,dy)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    print("Midpoint Line:", x3,"&", y3)
    
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
    
def main () :
    x1 = int (input ( "Enter X1: "))
    y1 = int (input ( "Enter Y1: "))
    x2 = int (input ( "Enter X2: ")) 
    y2 = int (input ("Enter Y2: "))
    DDALine (x1, y1, x2, y2)
    
if __name__ == '__main__':
    main()
            